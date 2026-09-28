## @package compute_experiment_similarity
#  论文用例相似度计算（按 experiment.json 实验设计）
#  职责：读 experiment.json 的 D_fixed / R_fixed 两组实验设计，对每组
#  deprecate × candidates 的每个组合，用 tokenBased 相似度算法计算
#  deprecated_api/<dep>.py（query）与 candidates/<cand>/*.py（候选）的相似度，
#  做 competition 排名（降序，相同分数共享名次、名次跳位，从 1 开始），
#  每个组合输出一个 json 到 result/<组>/<dep>-<cand>.json。
#  每个元素：{"api_name": <候选文件名，不含 .py>, "score": <相似度>, "rank": <名次>}。
#  性能：候选版本表示先并行 build 并 pickle 到 .build_cache/，跨组合复用，
#  避免 R_fixed 对同一 1.0.0 候选池重复 build。

import argparse
import json
import os
import pickle
import sys
from concurrent.futures import ProcessPoolExecutor

PEAR_ROOT = "/home/he/PEAR"
RECOMMEND_DIR = os.path.join(PEAR_ROOT, "Recommend")
if RECOMMEND_DIR not in sys.path:
    sys.path.insert(0, RECOMMEND_DIR)

from tokenBased import build_representation, similarity_from_representation  # noqa: E402

DEFAULT_CASE_DIR = os.path.join(
    PEAR_ROOT, "PreliminaryEvaluation", "paper_cases",
    "pandas.core.indexes.multi.MultiIndex.set_labels-"
    "pandas.core.indexes.multi.MultiIndex.set_codes",
)


def load_experiment(config_path):
    """读 experiment.json 返回 D_fixed / R_fixed 实验设计。

    输入参数：
        config_path (str)：experiment.json 绝对路径。
    返回值：
        dict：{"D_fixed": {"deprecate": ..., "candidates": ...},
               "R_fixed": {"deprecate": ..., "candidate": ...}}。
    异常：
        FileNotFoundError：配置文件不存在。
        ValueError：缺少 D_fixed / R_fixed 键。
    """
    with open(config_path, encoding="utf-8") as f:
        exp = json.load(f)
    for key in ("D_fixed", "R_fixed"):
        if key not in exp:
            raise ValueError(f"experiment.json 缺少 {key} 组")
    return exp


def build_combinations(experiment):
    """由实验设计展开 (组名, deprecate, candidate) 组合序列。

    D_fixed：deprecate 为单值，与 candidates 每个版本各组合一次。
    R_fixed：candidate 为单值，与 deprecate 每个版本各组合一次。

    输入参数：
        experiment (dict)：load_experiment 的返回。
    返回值：
        list[tuple[str, str, str]]：[(组名, deprecate 版本, candidate 版本), ...]。
    """
    combos = []
    d = experiment["D_fixed"]
    dep = d["deprecate"] if isinstance(d["deprecate"], str) else d["deprecate"][0]
    for cand in d["candidates"]:
        combos.append(("D_fixed", dep, cand))

    r = experiment["R_fixed"]
    cand = r["candidate"] if isinstance(r["candidate"], str) else r["candidate"][0]
    for dep in r["deprecate"]:
        combos.append(("R_fixed", dep, cand))
    return combos


def competition_rank(scores_desc):
    """按降序分数序列生成 competition 名次（1-based）。

    输入参数：
        scores_desc (list[float])：按降序排好的相似度序列。
    返回值：
        list[int]：与输入等长的名次序列。
    """
    ranks = []
    n = len(scores_desc)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and scores_desc[j + 1] == scores_desc[i]:
            j += 1
        for _ in range(i, j + 1):
            ranks.append(i + 1)
        i = j + 1
    return ranks


def _build_version_worker(args):
    """build 单个候选版本目录下全部 .py 的表示并 pickle 落盘。

    输入参数：
        args (tuple)：(version, cand_dir, cache_path)。
    返回值：
        tuple：(version, 成功数, 失败数)。
    """
    version, cand_dir, cache_path = args
    files = sorted(f for f in os.listdir(cand_dir) if f.endswith(".py"))
    cache = {}
    failed = 0
    for fname in files:
        try:
            with open(os.path.join(cand_dir, fname), encoding="utf-8") as f:
                src = f.read()
            cache[fname] = build_representation(src)
        except Exception as e:  # noqa: BLE001 —— 显式报出，不静默跳过
            print(f"[WARN] build 失败 {version}/{fname}: "
                  f"{type(e).__name__}: {e}", flush=True)
            failed += 1
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    with open(cache_path, "wb") as f:
        pickle.dump(cache, f)
    return version, len(cache), failed


def build_candidate_caches(unique_cand_versions, candidates_dir, cache_root):
    """并行 build 全部候选版本的表示，pickle 到 .build_cache/。

    输入参数：
        unique_cand_versions (list[str])：候选版本号列表（去重）。
        candidates_dir (str)：candidates 根目录。
        cache_root (str)：.build_cache 目录。
    返回值：
        dict：{version: cache_pkl 路径}。
    异常：
        FileNotFoundError：候选池目录不存在。
    """
    os.makedirs(cache_root, exist_ok=True)
    tasks = []
    for version in unique_cand_versions:
        cache_path = os.path.join(cache_root, f"{version}.pkl")
        if os.path.isfile(cache_path) and os.path.getsize(cache_path) > 0:
            continue  # 已缓存，跳过重复 build
        cand_dir = os.path.join(candidates_dir, version)
        if not os.path.isdir(cand_dir):
            raise FileNotFoundError(f"候选池目录不存在: {cand_dir}")
        tasks.append((version, cand_dir, cache_path))

    if tasks:
        workers = max(1, min(len(tasks), os.cpu_count() or 1))
        with ProcessPoolExecutor(max_workers=workers) as ex:
            for version, n, failed in ex.map(_build_version_worker, tasks):
                print(f"[build] {version}: {n} 个表示 (失败 {failed})", flush=True)

    return {v: os.path.join(cache_root, f"{v}.pkl")
            for v in unique_cand_versions}


def compute_pair(group, dep_version, cand_version, query_source, cand_cache,
                 result_dir):
    """计算单个组合的相似度并 competition 排名，写 json。

    输入参数：
        group (str)：组名 D_fixed / R_fixed。
        dep_version (str)：deprecate 版本号。
        cand_version (str)：candidate 版本号。
        query_source (str)：deprecate 源码。
        cand_cache (dict)：{文件名: 表示} 候选池表示缓存（key 含 .py）。
        result_dir (str)：result 根目录。
    返回值：
        str：写出的 json 路径。
    """
    query_repr = build_representation(query_source)
    rows = []
    for fname, repr_ in cand_cache.items():
        try:
            sim = similarity_from_representation(query_repr, repr_)
        except (TypeError, ValueError) as e:  # noqa: BLE001 —— 显式报出
            print(f"[WARN] 比较失败 {cand_version}/{fname}: "
                  f"{type(e).__name__}: {e}", flush=True)
            continue
        rows.append((fname, sim))

    rows.sort(key=lambda x: x[1], reverse=True)
    ranks = competition_rank([s for _, s in rows])
    records = [
        {"api_name": fname[:-3], "score": sim, "rank": rk}
        for (fname, sim), rk in zip(rows, ranks)
    ]

    out_dir = os.path.join(result_dir, group)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{dep_version}-{cand_version}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=1)
    return out_path


def main(argv=None):
    """入口：读实验设计 → build 候选缓存 → 逐组合计算排名落盘。

    输入参数：
        argv (Optional[list[str]])：命令行参数；None 用 sys.argv。
    返回值：
        int：0 全部成功；1 存在失败。
    """
    parser = argparse.ArgumentParser(
        description="按 experiment.json 计算论文用例相似度并输出到 result/")
    parser.add_argument("--case-dir", default=DEFAULT_CASE_DIR,
                        help="论文用例目录")
    args = parser.parse_args(argv)

    case_dir = args.case_dir
    deprecated_dir = os.path.join(case_dir, "deprecated_api")
    candidates_dir = os.path.join(case_dir, "candidates")
    result_dir = os.path.join(case_dir, "result")
    cache_root = os.path.join(case_dir, ".build_cache")

    experiment = load_experiment(os.path.join(case_dir, "experiment.json"))
    combos = build_combinations(experiment)
    unique_cand = sorted({cand for _, _, cand in combos})
    unique_dep = sorted({dep for _, dep, _ in combos})

    # 阶段1：build 候选版本表示缓存
    print(f"[1/2] build 候选版本表示（{len(unique_cand)} 个版本）...", flush=True)
    build_candidate_caches(unique_cand, candidates_dir, cache_root)

    # 阶段2：逐组合计算排名
    print(f"[2/2] 计算 {len(combos)} 个组合相似度排名...", flush=True)
    failed = []
    for group, dep_version, cand_version in combos:
        try:
            query_path = os.path.join(deprecated_dir, f"{dep_version}.py")
            if not os.path.isfile(query_path):
                raise FileNotFoundError(f"query 不存在: {query_path}")
            with open(query_path, encoding="utf-8") as f:
                query_source = f.read()
            cache_path = os.path.join(cache_root, f"{cand_version}.pkl")
            with open(cache_path, "rb") as f:
                cand_cache = pickle.load(f)
            out_path = compute_pair(group, dep_version, cand_version,
                                    query_source, cand_cache, result_dir)
            print(f"[ok] {group} {dep_version}-{cand_version} -> "
                  f"{out_path} ({len(cand_cache)} 候选)", flush=True)
        except Exception as e:  # noqa: BLE001 —— 显式报出，继续其余组合
            print(f"[FAIL] {group} {dep_version}-{cand_version}: "
                  f"{type(e).__name__}: {e}", flush=True)
            failed.append(f"{group}:{dep_version}-{cand_version}")

    if failed:
        print(f"\n完成，失败 {len(failed)} 个组合: {failed}")
        return 1
    print(f"\n完成，共 {len(combos)} 个组合全部成功")
    return 0


if __name__ == "__main__":
    sys.exit(main())
