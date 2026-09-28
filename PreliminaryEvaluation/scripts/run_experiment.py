# -*- coding: utf-8 -*-
"""实验脚本（并行版）：对 cases.xlsx 逐行调用统一引擎的两种消融模式，输出推荐列表与 Top-k 命中统计。

两种模式（见 Pipeline/engine.MODES）：
  - direct           ：无边界/无调整/无验证/无追踪（原 DirectBaseline）
  - full_pear        ：全机制（boundary + adjust + validation + BFS 继续追踪）

并行策略：
  - multiprocessing fork 启动，父进程一次性加载三个库的 KnowledgeBase，
    子进程通过 fork COW 继承（只读共享）。
  - 行级并行跑实验。每个 worker 进程使用自己的 worktree 根目录
    （/tmp/pear_worktrees_p{PID}），同一 process 内跨行复用 SourceProvider，
    Provider 通过 run_recommender(provider=...) 传入，避免每行重建。
  - 结果由主进程汇总写入 experiment_summary_top{top_k}.json 与两个模式目录。
"""

import argparse
import atexit
import json
import multiprocessing as mp
import os
import sys
import time

import pandas as pd

PEAR_ROOT = "/home/he/PEAR"
sys.path.insert(0, PEAR_ROOT)

from Tool.model import Task                                    # noqa: E402
from Tool.tool import SourceProvider, load_knowledge_base      # noqa: E402
from Pipeline.engine import MODE_NAMES, run_recommender         # noqa: E402

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------
CASES_XLSX = os.path.join(PEAR_ROOT, "PreliminaryEvaluation", "cases.xlsx")
KB_DIR = os.path.join(PEAR_ROOT, "LibAPIExtraction")
LIBRARIES_ROOT = os.path.join(PEAR_ROOT, "Libraries")
CACHE_DIR = os.path.join(PEAR_ROOT, "CodeCache")

TARGET_VERSION = {"pandas": "3.0.5", "matplotlib": "3.11.1", "django": "6.0.7"}

COL_VERSION = 1       # B：V_s 版本（Preceding stable PyPI release）
COL_OLD_FQN = 3       # D：弃用 API FQN（D_fqn）
COL_REPLACEMENT = 4   # E：替代 API FQN（R_fqn）
COL_API_TYPE = 5      # F：粒度（Granularity，英文）

# ---------------------------------------------------------------------------
# 进程级全局状态（fork 后每个 worker 独立一份）
# ---------------------------------------------------------------------------
_KBS = {}               # lib -> KnowledgeBase（fork COW 继承，只读共享）
_WORKER_PROVIDERS = {}  # lib -> SourceProvider（per-process 懒创建，跨行复用）
_TOP_K = 20                  # main() 按 --top-k 覆盖，fork 后 worker 继承
_K_LIST = [1, 3, 5, 10, 20]  # main() 按 _TOP_K 动态生成（统计 hit@k 用）


def _get_worker_provider(lib_name):
    """当前进程（worker）为 lib 创建/复用的 SourceProvider。

    每个 worker 用唯一 worktree 根（/tmp/pear_worktrees_p{PID}），避免跨进程
    worktree 冲突；同一 process 内跨行共享 provider。进程退出时 atexit 关闭。
    """
    if lib_name not in _WORKER_PROVIDERS:
        repo_path = os.path.join(LIBRARIES_ROOT, lib_name)
        provider = SourceProvider(
            lib_name, repo_path, CACHE_DIR,
            worktrees_root=f"/tmp/pear_worktrees_p{os.getpid()}")
        atexit.register(provider.close)
        _WORKER_PROVIDERS[lib_name] = provider
    return _WORKER_PROVIDERS[lib_name]


def hit_rank(ranked_list, target):
    """返回 target 在 ranked_list 中的 1-based 排名；不在则返回 -1。"""
    if target is None:
        return -1
    try:
        return ranked_list.index(target) + 1
    except ValueError:
        return -1


# ---------------------------------------------------------------------------
# 行级并行实验
# ---------------------------------------------------------------------------

def _run_row(task_arg):
    """worker 执行单行实验：对两种消融模式各跑一次统一引擎。"""
    lib_name = task_arg["lib"]
    old_fqn = task_arg["old_api_fqn"]
    source_version = task_arg["source_version"]
    api_type = task_arg["api_type"]       # 已在父进程转换为英文
    replacement = task_arg["replacement"]
    target_version = TARGET_VERSION[lib_name]
    kb = _KBS[lib_name]
    provider = _get_worker_provider(lib_name)

    task = Task(
        lib_name=lib_name, source_version=source_version,
        target_version=target_version, old_api_fqn=old_fqn,
        api_type=api_type, top_k=_TOP_K,
        lib_repo_path=os.path.join(LIBRARIES_ROOT, lib_name),
    )

    # ---- 两种模式 ----
    mode_results = {}   # mode -> {"result","fqns","status","sec"}
    for mode in MODE_NAMES:
        t0 = time.time()
        result = run_recommender(task, kb, cache_dir=CACHE_DIR,
                                 provider=provider, mode=mode)
        sec = time.time() - t0
        status = result.status
        fqns = [c.fqn for c in result.candidates]
        mode_results[mode] = {"result": result, "fqns": fqns,
                              "status": status, "sec": sec}

    pear_rank = hit_rank(mode_results["full_pear"]["fqns"], replacement)

    out = {
        "lib_name": lib_name,
        "source_version": source_version,
        "target_version": target_version,
        "old_api_fqn": old_fqn,
        "api_type": api_type,
        "real_replacement": replacement,
        "modes": {m: {"fqns": mode_results[m]["fqns"],
                      "status": mode_results[m]["status"],
                      "sec": mode_results[m]["sec"]}
                  for m in MODE_NAMES},
        "full_pear_hit@1": int(0 < pear_rank <= 1),
    }
    for m in MODE_NAMES:
        rank = hit_rank(mode_results[m]["fqns"], replacement)
        for k in _K_LIST:
            out[f"{m}_hit@{k}"] = int(0 < rank <= k)

    # 记录模式结果对象（供落盘）——不随 out 进汇总（含对象不可 pickle，仅 worker 内用）
    out["_mode_results"] = mode_results

    print(f"[{lib_name}] {old_fqn} | " +
          " | ".join(
              f"{m}:{mode_results[m]['status']}({len(mode_results[m]['fqns'])}个,"
              f"rank={hit_rank(mode_results[m]['fqns'], replacement)},"
              f"{mode_results[m]['sec']:.1f}s)"
              for m in MODE_NAMES),
          flush=True)
    return out


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------

def main():
    mp.set_start_method("fork")

    parser = argparse.ArgumentParser(description="PEAR 两种消融模式实验（并行版）")
    parser.add_argument("--limit", type=int, default=0,
                        help="每个 lib 只跑前 N 行（0=全部），用于冒烟测试")
    parser.add_argument("--libs", type=str, default="",
                        help="逗号分隔的 lib 过滤，空=全部")
    parser.add_argument("--workers", type=int, default=0,
                        help="并行 worker 数（默认 min(32, cpu_count)）")
    parser.add_argument("--top-k", type=int, default=20,
                        help="Top-k 推荐数量（默认 20）")
    args = parser.parse_args()

    libs_filter = [s.strip() for s in args.libs.split(",") if s.strip()]
    cpu = os.cpu_count() or 1
    n_workers = args.workers or max(1, min(88, cpu))

    global _TOP_K, _K_LIST
    _TOP_K = args.top_k
    _K_LIST = sorted(k for k in {1, 3, 5, 10, 20, _TOP_K} if k <= _TOP_K)

    # 读取 sheet，构造任务列表
    xl = pd.ExcelFile(CASES_XLSX)
    tasks = []  # list of dict (plain, picklable)
    for sheet in xl.sheet_names:
        if libs_filter and sheet not in libs_filter:
            continue
        df = xl.parse(sheet)
        if args.limit > 0:
            df = df.head(args.limit)
        for _, row in df.iterrows():
            old_fqn = str(row.iloc[COL_OLD_FQN]).strip()
            sv = str(row.iloc[COL_VERSION]).strip()
            api_type = str(row.iloc[COL_API_TYPE]).strip()
            repl = row.iloc[COL_REPLACEMENT]
            if pd.isna(repl):
                repl = None
            else:
                repl = str(repl).strip()
            tasks.append({
                "lib": sheet,
                "old_api_fqn": old_fqn,
                "source_version": sv,
                "api_type": api_type,
                "replacement": repl,
            })

    selected_libs = sorted({t["lib"] for t in tasks})
    print(f"库: {selected_libs}, 总行数: {len(tasks)}, workers: {n_workers}, "
          f"top_k: {_TOP_K}, 模式: {MODE_NAMES}")

    # 父进程加载 KB（fork 后子进程 COW 继承，只读共享）
    global _KBS
    for lib in selected_libs:
        _KBS[lib] = load_knowledge_base(lib, KB_DIR)

    # 行级并行实验
    print(f"\n开始行级并行实验（{len(tasks)} 行）...")
    t_start = time.time()
    with mp.Pool(processes=n_workers) as pool:
        results = pool.map(_run_row, tasks, chunksize=1)
    elapsed = time.time() - t_start
    print(f"\n完成，耗时 {elapsed:.0f}s ({elapsed/60:.1f}min)")

    # ---- 汇总统计（数值，不百分比）----
    all_detail = {}  # lib -> list of row dicts
    for row in results:
        all_detail.setdefault(row["lib_name"], []).append(row)

    summary_stats = {}  # lib -> {"n_rows", {mode: {"hit@k","no_definition"}}}
    for lib in selected_libs:
        rows = all_detail.get(lib, [])
        stat = {"n_rows": len(rows), "modes": {}}
        for m in MODE_NAMES:
            mstat = {}
            for k in _K_LIST:
                mstat[f"hit@{k}"] = sum(row[f"{m}_hit@{k}"] for row in rows)
            mstat["n_no_definition"] = sum(
                1 for row in rows if row["modes"][m]["status"] == "NO_DEFINITION")
            mstat["n_error"] = sum(
                1 for row in rows if row["modes"][m]["status"] == "ERROR")
            stat["modes"][m] = mstat
        summary_stats[lib] = stat

    total_n = sum(stat["n_rows"] for stat in summary_stats.values())
    total_stat = {"n_rows": total_n, "modes": {}}
    for m in MODE_NAMES:
        mstat = {}
        for k in _K_LIST:
            mstat[f"hit@{k}"] = sum(row[f"{m}_hit@{k}"] for row in results)
        mstat["n_no_definition"] = sum(
            1 for row in results if row["modes"][m]["status"] == "NO_DEFINITION")
        mstat["n_error"] = sum(
            1 for row in results if row["modes"][m]["status"] == "ERROR")
        total_stat["modes"][m] = mstat
    summary_stats["TOTAL"] = total_stat

    # ---- 写两个模式目录（一个推荐任务一个文件）----
    mode_dirs = {m: os.path.join(PEAR_ROOT, "PreliminaryEvaluation", m)
                 for m in MODE_NAMES}
    for m in MODE_NAMES:
        os.makedirs(mode_dirs[m], exist_ok=True)
    for i, row in enumerate(results):
        mode_results = row["_mode_results"]
        for m in MODE_NAMES:
            result = mode_results[m]["result"]
            record = _persist_record(result, m)
            with open(os.path.join(mode_dirs[m], f"{i:04d}_{row['lib_name']}.json"),
                      "w", encoding="utf-8") as f:
                json.dump(record, f, ensure_ascii=False, indent=2)

    # ---- 写汇总 json（数值不含百分比）----
    records = []
    for row in results:
        rec = {
            "lib_name": row["lib_name"],
            "source_version": row["source_version"],
            "target_version": row["target_version"],
            "old_api_fqn": row["old_api_fqn"],
            "api_type": row["api_type"],
            "real_replacement": row["real_replacement"],
        }
        for m in MODE_NAMES:
            rec[f"{m}_status"] = row["modes"][m]["status"]
            for k in _K_LIST:
                rec[f"{m}_hit@{k}"] = row[f"{m}_hit@{k}"]
        records.append(rec)
    summary_json = os.path.join(PEAR_ROOT, "PreliminaryEvaluation",
                                f"experiment_summary_top{_TOP_K}.json")
    with open(summary_json, "w", encoding="utf-8") as f:
        json.dump({"records": records, "summary": summary_stats},
                  f, ensure_ascii=False, indent=2)

    # ---- 控制台汇总（数值）----
    print("\n===== 汇总（hit@k / n   其中 NO_DEFINITION/ERROR）=====")
    for lib in selected_libs + ["TOTAL"]:
        s = summary_stats[lib]
        print(f"{lib:12s} n={s['n_rows']:3d}  " +
              "  ".join(
                  f"{m}:{s['modes'][m]['hit@5']}"
                  f"(nd={s['modes'][m]['n_no_definition']},"
                  f"err={s['modes'][m]['n_error']})" for m in MODE_NAMES))
    print(f"\n模式目录: " + ", ".join(f"{m}" for m in MODE_NAMES))
    print(f"汇总 json: {summary_json}")
    return 0


def _persist_record(result, mode: str) -> dict:
    """把单模式结果落盘为 JSON dict。

    单跳模式（direct）：只存最终排序候选（fqn/api_type/
    similarity），不含演化路径与 trace；Full PEAR 存完整（task/status/error/
    candidates/trace，候选含 evolution_path/local_scores）。
    """
    if mode == "full_pear":
        return result.to_dict()
    return {
        "task": result.task.to_dict(),
        "status": result.status,
        "candidates": [
            {"fqn": c.fqn, "api_type": c.api_type, "similarity": c.similarity}
            for c in result.candidates
        ],
    }


if __name__ == "__main__":
    sys.exit(main())
