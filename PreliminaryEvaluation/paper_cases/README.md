# Paper Cases

This directory contains the case discussed in the paper and the files needed to inspect and reproduce its similarity rankings.

## Case

The paper reports the mapping:

`pandas.MultiIndex.set_labels` → `pandas.MultiIndex.set_codes`

For source-level identification, the repository uses the corresponding fully qualified names (FQNs):

`pandas.core.indexes.multi.MultiIndex.set_labels` → `pandas.core.indexes.multi.MultiIndex.set_codes`

`set_labels` was deprecated in pandas 0.24.0. The source version used in the paper is the preceding stable release, \(V_s = 0.23.4\).

## Experiment Design

`experiment.json` defines two groups:

| Group | Fixed | Varied |
|---|---|---|
| `D_fixed` | query API from pandas 0.23.4 | target version, 0.24.0 → 3.0.0 |
| `R_fixed` | target version 1.0.0 | query version, 0.14.0 → 0.25.0 |

`D_fixed` varies the target-side API space while keeping the query fixed. `R_fixed` varies the historical representation of the query while keeping the target candidate pool fixed.

Pandas 1.0.0 is used as the fixed target in `R_fixed` because it is the first release in which `set_labels` is absent. Each combination ranks all method-level APIs present in the target version. The results below report the position of the documented replacement `set_codes` in these rankings.

## Structure

```text
paper_cases/
├── README.md
├── extract_case_apis.py
├── compute_experiment_similarity.py
└── pandas.core.indexes.multi.MultiIndex.set_labels-pandas.core.indexes.multi.MultiIndex.set_codes/
    ├── experiment.json
    ├── deprecated_api/
    ├── candidates/
    └── result/
```

- `experiment.json`: experiment configuration.
- `deprecated_api/`: versioned source code of `set_labels`.
- `candidates/`: method-level candidate APIs for each target version.
- `result/`: per-combination rankings and `summary.json`.
- `extract_case_apis.py`: regenerates the query APIs and candidate pools.
- `compute_experiment_similarity.py`: computes the rankings.

## Reproduction

Regenerate the experiment inputs:

```bash
python extract_case_apis.py
```

Compute the rankings:

```bash
python compute_experiment_similarity.py
```

The scripts expect the pandas repository under `Libraries/`.

> Both scripts currently use `PEAR_ROOT = "/home/he/PEAR"`. Change this path if the repository is located elsewhere.

The checked-in `deprecated_api/`, `candidates/`, and `result/` directories allow the case to be inspected without regenerating all intermediate files.

## Results

**`D_fixed`** — query fixed at 0.23.4; target version varies:

| Target version | 0.24.0 | 0.25.0 | 1.0.0 | 1.1.0 | 1.2.0 | 1.3.0 | 1.4.0 | 1.5.0 | 2.0.0 | 2.1.0 | 2.2.0 | 3.0.0 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rank | 1 | 1 | 1 | 1 | 1 | 64 | 30 | 21 | 4116 | 4265 | 5034 | 5067 |
| Score | 0.923 | 0.923 | 0.931 | 0.931 | 0.831 | 0.449 | 0.465 | 0.473 | 0.293 | 0.293 | 0.283 | 0.283 |

**`R_fixed`** — target fixed at 1.0.0; query version varies:

| Query version | 0.14.0 | 0.15.0 | 0.16.0 | 0.17.0 | 0.18.0 | 0.19.0 | 0.20.0 | 0.21.0 | 0.22.0 | 0.23.0 | 0.24.0 | 0.25.0 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Rank | 35 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 4719 | 4719 |
| Score | 0.466 | 0.885 | 0.931 | 0.931 | 0.931 | 0.931 | 0.931 | 0.931 | 0.931 | 0.931 | 0.220 | 0.220 |

The results show that similarity-based rankings can change substantially as either the target library or the query API evolves across versions.