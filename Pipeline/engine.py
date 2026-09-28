## @package engine
#  统一可配置推荐引擎(两种消融模式共享)
#  职责：把「get_boundary → resolve_api → recommend → 验证/追踪」编排成统一引擎，
#  用 4 个布尔开关(RecommenderConfig)驱动，2 种消融预设(MODES)只是不同开关组合：
#    - use_boundary   = Local boundary（定位相邻弃用边界 (vpre,vpost) 做局部推荐）
#    - use_adjust     = Object adjustment（resolve_api 更正 query 定义）
#    - use_validation = Target validation（候选须存在于 Vt 才入选）
#    - use_tracking   = Continued tracking（不在 Vt 的候选 BFS 继续追）
#  两个模式共享同一套候选生成/定义/相似度/排序实现(recommend)，只差在开关机制，
#  保证消融实验公平。原先各自独立的 run_pipeline(Full PEAR) 与 direct_baseline(Direct)
#  改为本引擎的薄封装，签名不变。

import heapq
from dataclasses import dataclass
from typing import List, Optional

from Tool.model import Candidate, KnowledgeBase, ResolvedApi, Result, Task
from Tool.tool import SourceProvider
from Adjust.getBoundary import get_boundary
from Adjust.resolveApi import resolve_api
from Recommend.recommend import recommend


@dataclass(frozen=True)
class RecommenderConfig:
    """统一引擎的四进制开关配置（见模块 docstring）。"""
    use_boundary: bool      # 定位 (vpre,vpost) 局部推荐
    use_adjust: bool        # resolve_api 更正 query 定义
    use_validation: bool    # 候选须存在于 Vt
    use_tracking: bool      # 不在 Vt 的候选 BFS 继续追


## 两种消融预设（按键名取用；模式列见模块 docstring）
MODES = {
    "direct":          RecommenderConfig(False, False, False, False),
    "full_pear":       RecommenderConfig(True,  True,  True,  True),
}


## 消融模式键的顺序列表（供实验遍历；保证 full_pear 末位）
MODE_NAMES = list(MODES.keys())


# ---------------------------------------------------------------------------
# 路径评分 / trace 辅助（自原 pipeline.py 迁入，逻辑不变）
# ---------------------------------------------------------------------------

def _path_score(scores: List[float]) -> float:
    """路径分数：各跳相似度连乘（空路径返回 1.0，为最上层哨兵值）。"""
    score = 1.0
    for s in scores:
        score *= s
    return score


def _final_score(c: Candidate) -> float:
    """候选最终评分：路径上各跳相似度连乘。"""
    return _path_score(c.local_scores)


def _trace_node(fqn: str, path_score: float, boundary: Optional[str] = None,
                vpre: Optional[str] = None, vpost: Optional[str] = None,
                resolved_fqn: Optional[str] = None,
                resolved_kind: Optional[str] = None,
                candidates: Optional[List[dict]] = None,
                entered_final: Optional[List[str]] = None,
                entered_iter: Optional[List[str]] = None,
                pruned: Optional[List[str]] = None,
                prune_bound: Optional[float] = None,
                dead_reason: Optional[str] = None) -> dict:
    """构造一条 BFS 轨迹节点（dict），随 Result.trace 序列化输出。"""
    return {
        "fqn": fqn,
        "path_score": round(path_score, 6),
        "boundary": boundary,
        "vpre": vpre,
        "vpost": vpost,
        "resolved_fqn": resolved_fqn,
        "resolved_kind": resolved_kind,
        "candidates": candidates or [],
        "entered_final": entered_final or [],
        "entered_iter": entered_iter or [],
        "pruned": pruned or [],
        "prune_bound": round(prune_bound, 6) if prune_bound is not None else None,
        "dead_reason": dead_reason,
    }


# ---------------------------------------------------------------------------
# 统一引擎入口
# ---------------------------------------------------------------------------

def run_recommender(task: Task, kb: Optional[KnowledgeBase] = None,
                    cache_dir: str = 'CodeCache',
                    provider: Optional[SourceProvider] = None,
                    mode: object = 'full_pear') -> Result:
    """按模式运行统一推荐引擎，返回最终 Result。

    输入参数：
        task (Task)：分析任务（Vs/Vt/old_api_fqn/api_type/top_k/lib_repo_path）。
        kb (Optional[KnowledgeBase])：内存知识库。仅 use_boundary / use_validation
            模式需要；Direct 模式(use_boundary=False, use_validation=False)可传 None。
        cache_dir (str)：完整定义缓存根目录，默认 'CodeCache'。
        provider (Optional[SourceProvider])：外部传入则复用（不创建不关闭），
            None 时内部创建并关闭。
        mode (object)：既可为 MODES 的字符串键（'direct'/
            'full_pear'），也可直接传 RecommenderConfig。
            默认 'full_pear'（与旧 run_pipeline 语义一致）。
    返回值：
        Result：status 见模型注释；candidates 为排序候选。单跳模式(Direct)
            仅含最终候选(fqn+sim)，trace 留空、不带演化路径；
            Full PEAR 保留完整 trace 与演化路径。
    异常：
        ValueError：use_boundary/use_validation 需要 kb 且 kb 为 None，或
            bool(source/target) 区间未提供 kb 时版本校验失败。
    """
    cfg = MODES[mode] if isinstance(mode, str) else mode
    own_provider = provider is None
    if own_provider:
        provider = SourceProvider(task.lib_name, task.lib_repo_path, cache_dir)
    try:
        if kb is None and (cfg.use_boundary or cfg.use_validation):
            raise ValueError("该模式需要 kb，但传入的 kb 为 None")
        if cfg.use_boundary:
            _require_versions(task, kb)
        if cfg.use_tracking:
            return _run_full_pear(task, kb, cfg, provider)
        return _run_single_hop(task, kb, cfg, provider)
    except Exception as e:
        print(f"[engine] 分析失败: {type(e).__name__}: {e}")
        return Result(task=task, status='ERROR',
                      error=f"{type(e).__name__}: {e}")
    finally:
        if own_provider:
            provider.close()


def _require_versions(task: Task, kb: KnowledgeBase) -> None:
    """校验 task 的 Vs/Vt 均在 kb.versions 序列中。"""
    versions = kb.versions
    if task.source_version not in versions or task.target_version not in versions:
        raise ValueError(
            f"Vs/Vt 不在知识库版本序列中: {task.source_version} / {task.target_version}")


def _window(task: Task, kb: KnowledgeBase) -> List[str]:
    """截取 [Vs, Vt] 区间版本序列（get_boundary 在其上做 index 查找）。"""
    versions = kb.versions
    lo = versions.index(task.source_version)
    hi = versions.index(task.target_version)
    return versions[lo: hi + 1]


def _resolve_query(fqn: str, vpre: str, source_version: str,
                   task: Task, kb: KnowledgeBase, provider: SourceProvider,
                   cfg: RecommenderConfig) -> tuple:
    """按 use_adjust 决定 query 相似度定义取哪份，返回 (resolved_or_None, dead_reason)。

    输入参数：
        fqn (str)：待分析 API（根 = old_api_fqn；迭代分支 = 候选 FQN）。
        vpre (str)：query 所在版本（边界定位的 vpre，Direct 时 = Vs）。
        source_version (str)：起点版本（根 = Vs；迭代分支 = 上一跳 vpost）。
        task (Task)：提供 api_type。
        kb (KnowledgeBase)：resolve_api 需要。
        provider (SourceProvider)：get_api（不 adjust 时取定义）。
        cfg (RecommenderConfig)：use_adjust 开关。
    返回值：
        Tuple[Optional[ResolvedApi], Optional[str]]：成功 (resolved, None)；
            失败 (None, dead_reason)，dead_reason ∈ {'unknown', 'no_definition'} 之一。
    """
    if cfg.use_adjust:
        resolved = resolve_api(fqn, vpre, source_version, task.api_type, kb, provider)
        if resolved.kind == 'unknown' or not resolved.definition:
            return None, (resolved.kind or 'no_definition')
        return resolved, None
    raw = provider.get_api(fqn, task.api_type, vpre)
    if raw is None or not raw.strip():
        return None, 'no_definition'
    return ResolvedApi(original_fqn=fqn, resolved_fqn=fqn, kind='direct',
                       definition=raw), None


# ---------------------------------------------------------------------------
# 单跳模式（Direct；use_tracking=False）
# ---------------------------------------------------------------------------

def _run_single_hop(task: Task, kb: Optional[KnowledgeBase],
                    cfg: RecommenderConfig, provider: SourceProvider) -> Result:
    """单跳推荐（不追踪演化链）：定位边界 → 取定义 → 推荐 → 可选验证 → 排序。

    query 自带（original_fqn）在 data 保证下不在 vpost/Vt，为消融一致性统一
    不排除（exclude_original=False）；单跳结果只含最终排序候选，trace 留空。
    """
    # 1) 边界
    if cfg.use_boundary:
        b = get_boundary(task.old_api_fqn, task.source_version,
                         task.target_version, kb, _window(task, kb))
        if b.status == 'NOT_DEPRECATED':
            return Result(task=task, status='NOT_DEPRECATED')
        if b.status == 'NOT_FOUND':
            return Result(task=task, status='NOT_FOUND')
        vpre, vpost = b.vpre, b.vpost
    else:
        vpre, vpost = task.source_version, task.target_version

    # 2) 定义
    resolved, dead = _resolve_query(task.old_api_fqn, vpre, task.source_version,
                                    task, kb, provider, cfg)
    if dead is not None:
        status = 'NO_DEFINITION' if dead == 'no_definition' else 'NO_CANDIDATE'
        return Result(task=task, status=status)

    # 3) 推荐（三模式同一实现；统一不排除 query）
    repr_cache: dict = {}
    cands = recommend(resolved, vpre, vpost, task.api_type, kb, provider,
                      task.top_k, repr_cache=repr_cache, exclude_original=False)

    # 4) 可选目标验证：仅保留存在于 Vt 的候选
    if cfg.use_validation:
        cands = [c for c in cands
                 if kb is not None and kb.exists(c.fqn, task.target_version)]
    if not cands:
        return Result(task=task, status='NO_CANDIDATE')

    ranked = cands[: task.top_k]
    return Result(task=task, status='OK', candidates=ranked)


# ---------------------------------------------------------------------------
# 全链路模式（Full PEAR；use_tracking=True）
# ---------------------------------------------------------------------------

def _run_full_pear(task: Task, kb: KnowledgeBase, cfg: RecommenderConfig,
                   provider: SourceProvider) -> Result:
    """BFS 迭代展开演化链并汇总最终推荐（原 run_pipeline 主体迁入）。

    逻辑与旧 pipeline.py 完全一致，仅 recommend 显式 exclude_original=False
    （data 保证下 query 不在候选，排除与否无差；保持三模式同一推荐实现）。
    """
    window = _window(task, kb)
    trace: List[dict] = []

    # 优先队列（小顶堆）：(-路径分数, 自增序号, fqn, pos, path, scores)
    seq = 0
    queue = [(-1.0, seq, task.old_api_fqn, task.source_version, [], [])]
    visited = set()
    final: List[Candidate] = []
    final_heap: List[float] = []
    repr_cache: dict = {}

    while queue:
        neg_score, _seq, fqn, pos, path, scores = heapq.heappop(queue)
        cur_score = -neg_score
        if fqn in visited:
            continue
        visited.add(fqn)
        if len(final_heap) >= task.top_k and cur_score < final_heap[0]:
            trace.append(_trace_node(fqn=fqn, path_score=cur_score,
                                     prune_bound=final_heap[0],
                                     dead_reason='pruned_at_pop'))
            continue

        boundary = get_boundary(fqn, pos, task.target_version, kb, window)
        if boundary.status == 'NOT_DEPRECATED':
            if fqn == task.old_api_fqn:
                trace.append(_trace_node(fqn=fqn, path_score=cur_score,
                                         boundary='NOT_DEPRECATED',
                                         dead_reason='not_deprecated_root'))
                return Result(task=task, status='NOT_DEPRECATED', trace=trace)
            trace.append(_trace_node(fqn=fqn, path_score=cur_score,
                                     boundary='NOT_DEPRECATED',
                                     dead_reason='not_deprecated'))
            continue
        if boundary.status == 'NOT_FOUND':
            if fqn == task.old_api_fqn:
                trace.append(_trace_node(fqn=fqn, path_score=cur_score,
                                         boundary='NOT_FOUND',
                                         dead_reason='not_found_root'))
                return Result(task=task, status='NOT_FOUND', trace=trace)
            trace.append(_trace_node(fqn=fqn, path_score=cur_score,
                                     boundary='NOT_FOUND',
                                     dead_reason='not_found'))
            continue

        resolved, dead = _resolve_query(fqn, boundary.vpre, pos,
                                        task, kb, provider, cfg)
        if dead is not None:
            trace.append(_trace_node(
                fqn=fqn, path_score=cur_score, boundary=boundary.status,
                vpre=boundary.vpre, vpost=boundary.vpost,
                resolved_fqn=resolved.resolved_fqn if resolved else fqn,
                resolved_kind=resolved.kind if resolved else dead,
                dead_reason=dead))
            continue

        cands = recommend(resolved, boundary.vpre, boundary.vpost,
                          task.api_type, kb, provider, task.top_k,
                          repr_cache=repr_cache, exclude_original=False)
        if not cands:
            trace.append(_trace_node(
                fqn=fqn, path_score=cur_score, boundary=boundary.status,
                vpre=boundary.vpre, vpost=boundary.vpost,
                resolved_fqn=resolved.resolved_fqn,
                resolved_kind=resolved.kind,
                dead_reason='empty_recommend'))
            continue

        cand_items: List[dict] = []
        entered_final: List[str] = []
        entered_iter: List[str] = []
        pruned: List[str] = []
        for c in cands:
            cand_items.append({"fqn": c.fqn, "similarity": round(c.similarity, 6)})
            new_path = path + [c.fqn]
            new_scores = scores + [c.similarity]
            new_score = _path_score(new_scores)
            if kb.exists(c.fqn, task.target_version):
                entered_final.append(c.fqn)
                final.append(Candidate(
                    fqn=c.fqn, api_type=c.api_type, similarity=0.0,
                    evolution_path=new_path, local_scores=new_scores))
                heapq.heappush(final_heap, new_score)
                if len(final_heap) > task.top_k:
                    heapq.heappop(final_heap)
            else:
                if len(final_heap) >= task.top_k and new_score < final_heap[0]:
                    pruned.append(c.fqn)
                    continue
                entered_iter.append(c.fqn)
                seq += 1
                heapq.heappush(queue, (-new_score, seq, c.fqn, boundary.vpost,
                                       new_path, new_scores))
        trace.append(_trace_node(
            fqn=fqn, path_score=cur_score, boundary=boundary.status,
            vpre=boundary.vpre, vpost=boundary.vpost,
            resolved_fqn=resolved.resolved_fqn, resolved_kind=resolved.kind,
            candidates=cand_items, entered_final=entered_final,
            entered_iter=entered_iter, pruned=pruned,
            prune_bound=(final_heap[0] if len(final_heap) >= task.top_k else None)))

    if not final:
        return Result(task=task, status='NO_CANDIDATE', trace=trace)

    merged: dict = {}
    for c in final:
        score = _final_score(c)
        if c.fqn not in merged or score > _final_score(merged[c.fqn]):
            c.similarity = score
            merged[c.fqn] = c
    ranked = sorted(merged.values(), key=_final_score, reverse=True)[: task.top_k]
    return Result(task=task, status='OK', candidates=ranked, trace=trace)