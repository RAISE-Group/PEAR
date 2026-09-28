# -*- coding: utf-8 -*-
"""配对显著性检验脚本：Direct vs PEAR 在同一批弃用 API → 替代 API mapping 上的
Top-k 命中（0/1 配对二分数据）做 McNemar 检验，判断 PEAR 是否显著优于 Direct。

数据来源：run_experiment.py 生成的 PreliminaryEvaluation/experiment_summary_top{top_k}.json，
每条记录含 direct_hit@k 与 full_pear_hit@k（均为 0/1）。脚本按 lib_name 分组，
对总体（TOTAL）与每个库分别统计 2×2 列联表并做检验。

仅依赖 Python 标准库（json / math / argparse / os），无第三方依赖。
用法：python scripts/paired_significance.py [--summary <json>] [--k 1,5,10]
"""

import argparse
import json
import math
import os


def _binomial_tail_le(n, x, p=0.5):
    """二项分布下尾累积概率 P(Bin(n, p) <= x)。"""
    return sum(math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
               for i in range(0, x + 1))


def mcnemar_exact(b, c):
    """McNemar 精确检验（基于 discordant 配对数的二项分布）。

    输入参数：
        b (int)：仅 Direct 命中、PEAR 未命中的配对数。
        c (int)：仅 PEAR 命中、Direct 未命中的配对数。
    返回：
        tuple[float, float]：(双尾 exact p, 单尾 PEAR>Direct exact p)。
        双尾 p = 2 * P(Bin(b+c, 0.5) <= min(b, c))，上限截断到 1.0；
        单尾 p = P(Bin(b+c, 0.5) >= c)。b+c=0（无 discordant 对）时返回 (1.0, 1.0)。
    """
    n = b + c
    if n == 0:
        return 1.0, 1.0
    two_sided = min(2.0 * _binomial_tail_le(n, min(b, c)), 1.0)
    one_sided = sum(math.comb(n, i) for i in range(c, n + 1)) / (2 ** n)
    return two_sided, one_sided


def mcnemar_asymptotic(b, c):
    """McNemar 连续性校正卡方近似检验。

    输入参数：
        b (int)：仅 Direct 命中数。
        c (int)：仅 PEAR 命中数。
    返回：
        tuple[float, float]：(χ² 统计量, p 值)。χ² = (|b-c|-1)² / (b+c)，df=1，
        p = erfc(√(χ²/2))。b+c=0 时返回 (0.0, 1.0)。
    """
    n = b + c
    if n == 0:
        return 0.0, 1.0
    chi2 = ((abs(b - c) - 1.0) ** 2) / n
    p = math.erfc(math.sqrt(chi2 / 2.0))
    return chi2, p


def contingency(records, k):
    """统计 records 在 Top-k 命中上的 Direct vs PEAR 2×2 列联表。

    输入参数：
        records (list[dict])：experiment_summary 中的 records 列表。
        k (int)：Top-k 阈值。
    返回：
        tuple[int,int,int,int]：(a, b, c, d)，a=两者均命中，b=仅 Direct 命中，
        c=仅 PEAR 命中，d=两者均未命中。
    异常：
        KeyError：records 中缺少 direct_hit@k 或 full_pear_hit@k 字段时抛出。
    """
    a = b = c = d = 0
    for r in records:
        dh = r[f"direct_hit@{k}"]
        ph = r[f"full_pear_hit@{k}"]
        if dh and ph:
            a += 1
        elif dh and not ph:
            b += 1
        elif not dh and ph:
            c += 1
        else:
            d += 1
    return a, b, c, d


def _stars(p):
    """按双尾 p 值返回显著性标注。"""
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return "n.s."


def _fmt_p(p):
    """p 值格式化：小于 0.0001 时用科学计数法，否则保留 4 位小数。"""
    return f"{p:.2e}" if p < 0.0001 else f"{p:.4f}"


def print_block(title, rows):
    """打印某个 Top-k 指标下各分组的检验结果表。

    输入参数：
        title (str)：表标题，如 "Hit@1"。
        rows (list[tuple])：每行为
            (组别, N, b, c, 双尾p, 单尾p, chi2, chi2_p, 判定)。
    返回：
        None。
    """
    print(f"\n===== Top-k 指标：{title} =====")
    header = (f"{'Group':<12} {'N':>5} {'b(Dir胜)':>9} {'c(PEAR胜)':>10} "
              f"{'p_exact(双尾)':>14} {'p(单尾PEAR>D)':>14} "
              f"{'chi2':>8} {'p_chi2':>9}  判定")
    print(header)
    print("-" * len(header))
    for group, n, b, c, p2, p1, chi2, pc, sig in rows:
        print(f"{group:<12} {n:>5} {b:>9} {c:>10} {_fmt_p(p2):>14} "
              f"{_fmt_p(p1):>14} {chi2:>8.2f} {_fmt_p(pc):>9}  {sig}")


def run_test(records, k_list):
    """对 records 做 Direct vs PEAR 的 McNemar 检验并打印全部结果。

    输入参数：
        records (list[dict])：experiment_summary 中的 records 列表。
        k_list (list[int])：要检验的 Top-k 阈值列表。
    返回：
        dict：{k: {group: {b, c, p_exact, p_1tail, chi2, p_chi2}}}，供调用方复用。
    异常：
        KeyError：records 中缺少所需 hit@k 字段时抛出。
    """
    # 分组：按 lib_name，另加 TOTAL
    groups = {}
    for r in records:
        groups.setdefault(r["lib_name"], []).append(r)
    ordered = ["TOTAL"] + sorted(groups.keys())
    groups["TOTAL"] = records

    # 预先校验所有需要的字段存在，缺失则一次性报错（不静默取默认值）
    required = {f"{p}_hit@{k}" for k in k_list
                for p in ("direct", "full_pear")}
    sample = records[0]
    missing = required - set(sample.keys())
    if missing:
        raise KeyError(f"汇总记录缺少字段: {sorted(missing)}")

    out = {}
    for k in k_list:
        rows = []
        out_k = {}
        for group in ordered:
            recs = groups[group]
            a, b, c, d = contingency(recs, k)
            p2, p1 = mcnemar_exact(b, c)
            chi2, pc = mcnemar_asymptotic(b, c)
            rows.append((group, len(recs), b, c, p2, p1, chi2, pc, _stars(p2)))
            out_k[group] = {"a": a, "b": b, "c": c, "d": d,
                            "p_exact": p2, "p_1tail": p1,
                            "chi2": chi2, "p_chi2": pc}
        print_block(f"Hit@{k}", rows)
        out[k] = out_k
    return out


def main():
    """解析命令行、读取汇总 JSON、执行 McNemar 检验并打印结果。"""
    parser = argparse.ArgumentParser(
        description="Direct vs PEAR 配对显著性检验（McNemar）")
    default_summary = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "experiment_summary_top10.json")
    parser.add_argument("--summary", default=default_summary,
                        help="experiment_summary json 路径")
    parser.add_argument("--k", default="1,5,10",
                        help="逗号分隔的 Top-k 阈值（默认 1,5,10）")
    args = parser.parse_args()

    if not os.path.exists(args.summary):
        raise FileNotFoundError(f"汇总文件不存在: {args.summary}")
    k_list = [int(x) for x in args.k.split(",") if x.strip()]

    with open(args.summary, encoding="utf-8") as f:
        data = json.load(f)
    records = data["records"]

    print(f"数据: {args.summary}")
    print(f"mapping 数: {len(records)}，检验指标: {sorted(k_list)}")
    print("注：b = 仅 Direct 命中的配对数，c = 仅 PEAR 命中的配对数；"
          "p_exact 为 McNemar 精确双尾，p(单尾) 检验 PEAR>Direct；"
          "判定标注 *<0.05 **<0.01 ***<0.001")

    run_test(records, k_list)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
