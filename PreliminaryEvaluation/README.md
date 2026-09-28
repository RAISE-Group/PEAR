# PreliminaryEvaluation

This directory contains the evaluation data and results for PEAR. The preliminary evaluation includes **161 deprecated API–replacement API mappings** from Pandas, Matplotlib, and Django.

## Structure

```text
PreliminaryEvaluation/
├── cases.xlsx
├── paper_cases/
├── direct/
├── full_pear/
└── scripts/
    ├── run_experiment.py
    └── paired_significance.py
```

- `cases.xlsx`: the 161 evaluation cases.
- `paper_cases/`: cases discussed in the paper. See [`paper_cases/README.md`](./paper_cases/README.md) for detailed descriptions.
- `direct/`: results of the Direct method.
- `full_pear/`: results of PEAR.
- `scripts/run_experiment.py`: script for reproducing the Direct and PEAR results.
- `scripts/paired_significance.py`: script for the paired significance tests between Direct and PEAR.

## Evaluation Cases

Each sheet in `cases.xlsx` corresponds to one library (`pandas`, `matplotlib`, or `django`) and contains the following columns:

| Column | Description |
|---|---|
| `library_name` | Library name |
| `Preceding stable PyPI release` | Source version \(V_s\) |
| `Original Record Entry` | Original deprecation record |
| `D_fqn` | Fully qualified name of the deprecated API |
| `R_fqn` | Fully qualified name of the documented replacement API |
| `Granularity` | API granularity (`class`, `function`, or `method`) |
| `Deprecated API Location` | Source location of the deprecated API |
| `Replacement API Location` | Source location of the replacement API |
| `D_fqn exists in <V_t>?` | Whether the deprecated API exists in \(V_t\) |
| `R_fqn exists in <V_t>?` | Whether the replacement API exists in \(V_t\) |

The target versions are Pandas 3.0.5, Matplotlib 3.11.1, and Django 6.0.7.

## Methods

| Method | Description |
|---|---|
| **Direct** | Uses the deprecated API in \(V_s\) as the query and ranks candidates directly in \(V_t\). |
| **PEAR** | Applies removal-boundary localization, relation resolution, and propagation toward \(V_t\). |

## Reproduction

Run the evaluation with:

```bash
python scripts/run_experiment.py --top-k 10
```

The experiment requires the library source code under `Libraries/`.

> `run_experiment.py` currently uses `PEAR_ROOT = "/home/he/PEAR"`. Change this path if the repository is located elsewhere.

To reproduce the significance tests reported below, run:

```bash
python scripts/paired_significance.py
```

The script reads `experiment_summary_top10.json`, produced by `run_experiment.py`, and reports paired **McNemar** tests for `TOTAL` and each library at Hit@1, Hit@5, and Hit@10.

Use `--summary <json>` to specify a different summary file and `--k 1,5,10` to select the metrics. The selected \(k\) values must be present in the summary file as `*_hit@k` fields. For example, `--top-k 10` generates Hit@1, Hit@3, Hit@5, and Hit@10. The significance script uses only the Python standard library and does not write output files.

## Results

Overall results on the 161 evaluation cases:

| Method | Hit@1 | Hit@5 | Hit@10 |
|---|---:|---:|---:|
| Direct | 24.2% (39/161) | 34.2% (55/161) | 37.9% (61/161) |
| **PEAR** | **36.6% (59/161)** | **46.6% (75/161)** | **48.4% (78/161)** |

Per-library results. Hit@\(k\) values are hit counts out of the number of cases in that library (shown in parentheses).  
Improvement is the relative improvement of PEAR over Direct, i.e. (PEAR − Direct) / Direct.

| Library | Method | Hit@1 | Hit@5 | Hit@10 |
|---|---|---|---|---|
| pandas (50) | Direct | 7 | 11 | 12 |
|  | PEAR | 18 | 23 | 23 |
|  | Improvement | +157.1% | +109.1% | +91.7% |
| matplotlib (60) | Direct | 12 | 20 | 24 |
|  | PEAR | 15 | 24 | 26 |
|  | Improvement | +25.0% | +20.0% | +8.3% |
| django (51) | Direct | 20 | 24 | 25 |
|  | PEAR | 26 | 28 | 29 |
|  | Improvement | +30.0% | +16.7% | +16.0% |

### Significance

Paired **McNemar** tests (exact binomial, Direct vs PEAR) are performed on the same 161 mappings.  
`b` denotes cases hit by Direct only, and `c` denotes cases hit by PEAR only.  
The one-sided p-value tests the alternative "PEAR > Direct". Sig. is based on the two-sided p-value (\* p < 0.05, \*\* p < 0.01, \*\*\* p < 0.001).

| Metric | Group | b | c | p (two-sided) | p (one-sided) | Sig. |
|---|---|---:|---:|---:|---:|---|
| Hit@1 | Total | 4 | 24 | 0.0002 | 9.0e-05 | *** |
| Hit@1 | pandas | 2 | 13 | 0.0074 | 0.0037 | ** |
| Hit@1 | django | 0 | 6 | 0.0312 | 0.0156 | * |
| Hit@1 | matplotlib | 2 | 5 | 0.4531 | 0.2266 | n.s. |
| Hit@5 | Total | 1 | 21 | 1.1e-05 | 5.5e-06 | *** |
| Hit@5 | pandas | 0 | 12 | 0.0005 | 0.0002 | *** |
| Hit@5 | django | 0 | 4 | 0.1250 | 0.0625 | n.s. |
| Hit@5 | matplotlib | 1 | 5 | 0.2188 | 0.1094 | n.s. |
| Hit@10 | Total | 0 | 17 | 1.5e-05 | 7.6e-06 | *** |
| Hit@10 | pandas | 0 | 11 | 0.0010 | 0.0005 | *** |
| Hit@10 | django | 0 | 4 | 0.1250 | 0.0625 | n.s. |
| Hit@10 | matplotlib | 0 | 2 | 0.5000 | 0.2500 | n.s. |

PEAR significantly outperforms Direct overall at all three \(k\) values and on pandas. On django, the gain is significant only at Hit@1; on matplotlib, the differences are not statistically significant.