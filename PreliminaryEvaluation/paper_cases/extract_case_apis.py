## @package extract_case_apis
#  论文用例 API 提取脚本（experiment.json 驱动）
#  职责：读用例目录下 experiment.json 的 D_fixed / R_fixed 设计，确定涉及的
#  版本集合，对每个版本从本地库仓库 checkout 该版本源码，按 method 粒度提取：
#    1) candidates/<版本>/<FQN>.py —— 该版本全部方法粒度 API，一个方法一个文件
#    2) deprecated_api/<版本>.py   —— 弃用 API（D_fqn）在该版本的源码
#  文件内容 = 该方法 AST 节点经 ast.unparse 归一化后的文本（不做公开别名缩短，
#  FQN 用源码路径形式，如 pandas.core.indexes.multi.MultiIndex.set_codes），
#  与用例目录中已有机生产物格式一致。
#
#  提取口径：
#    - 只取类体内定义的方法；__init__ / __new__ / __call__ 不单列
#    - .py 中带 @overload 的方法跳过；.pyi 存根中的方法照收
#    - 同一 FQN 同时存在于 .py 与 .pyi 时，以 .py 定义为准
#    - 弃用 API 按「类名 + 方法名」定位：其所在模块会随版本迁移，
#      不能由 FQN 直接拼出源码路径
#
#  版本来源：
#    candidates 版本 = D_fixed.candidates ∪ {R_fixed.candidate}
#    deprecated_api 版本 = {D_fixed.deprecate} ∪ R_fixed.deprecate
#
#  依赖 Knowledge.getVersion（版本号 ↔ git tag）与 Knowledge.getSource（worktree 切版本），
#  与 Knowledge.build 的产物构建走同一套底座。
#
#  用法：
#    python extract_case_apis.py [--case-dir DIR] [--repo PATH] [--lib pandas]
#                                [--deprecated-fqn D_fqn] [--versions 1.0.0,1.1.0]
#                                [--jobs N] [--worktrees-root DIR]
#                                [--skip-candidates | --skip-deprecated]

import argparse
import ast
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Dict, Iterator, List, Optional, Tuple

PEAR_ROOT = "/home/he/PEAR"
if PEAR_ROOT not in sys.path:
    sys.path.insert(0, PEAR_ROOT)

from Knowledge.getSource import checkout_version, remove_worktree, worktree_path  # noqa: E402
from Knowledge.getVersion import list_versions  # noqa: E402

DEFAULT_CASE_DIR = os.path.join(
    PEAR_ROOT, "PreliminaryEvaluation", "paper_cases",
    "pandas.core.indexes.multi.MultiIndex.set_labels-"
    "pandas.core.indexes.multi.MultiIndex.set_codes",
)
DEFAULT_LIB = "pandas"

## 不单独产出的方法名
#  __init__ / __new__ / __call__ 用于刻画类自身的 API，不另立方法条目；
#  候选池沿用该约定，故这三个名字不产出文件。
_CLASS_LEVEL_METHODS = frozenset({'__init__', '__new__', '__call__'})


# ---------------------------------------------------------------------------
# 实验设计与版本集合
# ---------------------------------------------------------------------------

def load_experiment(config_path: str) -> dict:
    """读 experiment.json，返回 D_fixed / R_fixed 两组实验设计。

    输入参数：
        config_path (str)：experiment.json 路径。
    返回值：
        dict：{"D_fixed": {...}, "R_fixed": {...}}。
    异常：
        FileNotFoundError：配置文件不存在。
        ValueError：缺少 D_fixed / R_fixed 键。
    """
    with open(config_path, encoding="utf-8") as f:
        exp = json.load(f)
    for key in ("D_fixed", "R_fixed"):
        if key not in exp:
            raise ValueError(f"experiment.json 缺少 {key} 组: {config_path}")
    return exp


def _as_list(value) -> List[str]:
    """把实验设计字段统一成列表（单值为 str 时包成单元素列表）。"""
    if isinstance(value, str):
        return [value]
    return list(value)


def collect_versions(experiment: dict) -> Tuple[List[str], List[str]]:
    """由实验设计推导需要提取的 candidate / deprecated 版本集合。

    输入参数：
        experiment (dict)：load_experiment 的返回。
    返回值：
        Tuple[List[str], List[str]]：(candidates 版本, deprecated 版本)，
            均按版本号升序去重。
    """
    d = experiment["D_fixed"]
    r = experiment["R_fixed"]
    cand = set(_as_list(d["candidates"])) | set(_as_list(r["candidate"]))
    dep = set(_as_list(d["deprecate"])) | set(_as_list(r["deprecate"]))
    key = _version_key
    return sorted(cand, key=key), sorted(dep, key=key)


def _version_key(version: str) -> Tuple[int, ...]:
    """版本号字符串 → 可比较数字元组。"""
    return tuple(int(part) for part in version.split('.'))


def parse_case_name(case_dir: str) -> Tuple[str, str]:
    """由用例目录名解析 (弃用 API FQN, 替代 API FQN)。

    目录名形如 "<D_fqn>-<R_fqn>"。

    输入参数：
        case_dir (str)：用例目录路径（可用尾部带 / 的形式）。
    返回值：
        Tuple[str, str]：(D_fqn, R_fqn)。
    异常：
        ValueError：目录名不是恰好两段（无法确定 D/R 分界）时抛出，
            此时应改用 --deprecated-fqn 显式指定。
    """
    name = os.path.basename(os.path.normpath(case_dir))
    parts = name.split('-')
    if len(parts) != 2:
        raise ValueError(
            f"用例目录名无法解析出 D/R 分界（需形如 D_fqn-R_fqn）: {name}；"
            f"请用 --deprecated-fqn 显式指定弃用 API")
    return parts[0], parts[1]


# ---------------------------------------------------------------------------
# 源码 → 方法粒度 API
# ---------------------------------------------------------------------------

def _iter_class_methods(class_node: ast.ClassDef,
                        prefix: str) -> Iterator[Tuple[str, ast.AST]]:
    """递归收集类节点下的方法（含嵌套类的方法），产出 (FQN, 节点)。

    输入参数：
        class_node (ast.ClassDef)：类定义节点。
        prefix (str)：该类已累积的 FQN 前缀（模块名或 模块名.外层类名）。
    返回值：
        Iterator[Tuple[str, ast.AST]]：方法 FQN 与其 AST 节点。
    """
    for node in class_node.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name in _CLASS_LEVEL_METHODS:
                continue
            yield f"{prefix}.{node.name}", node
        elif isinstance(node, ast.ClassDef):
            yield from _iter_class_methods(node, f"{prefix}.{node.name}")


def extract_methods_from_source(source: str, module: str,
                                skip_overload: bool = False) -> Dict[str, str]:
    """从单个源文件文本中提取全部方法粒度 API。

    只取类体内定义的方法（含嵌套类的方法）：类属性、模块级函数、类本身
    都不在候选池内；__init__ / __new__ / __call__ 见 _CLASS_LEVEL_METHODS。

    输入参数：
        source (str)：源文件文本。
        module (str)：该文件对应的模块路径，如 pandas.core.indexes.multi。
        skip_overload (bool)：是否跳过带 @overload 的方法。.py 文件为 True
            （重载分支只是类型标注，不是独立 API），.pyi 存根为 False。
    返回值：
        Dict[str, str]：{方法 FQN: ast.unparse 归一化后的源码文本}。
    异常：
        SyntaxError：源文件无法解析时抛出（调用方需显式处理并汇报）。
    """
    tree = ast.parse(source)
    out: Dict[str, str] = {}
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            for fqn, func in _iter_class_methods(node, f"{module}.{node.name}"):
                if skip_overload and any(
                        'overload' in ast.unparse(d)
                        for d in func.decorator_list):
                    continue
                out[fqn] = ast.unparse(func)
    return out


def resolve_package_root(lib_path: str, lib_name: str) -> str:
    """探测库包目录（遍历范围与模块前缀基准）。

    优先同名包目录（pandas/django 位于仓库根下），其次 lib/{lib_name}
    布局（matplotlib 为 lib/matplotlib），否则退回源码根。

    输入参数：
        lib_path (str)：版本源码根目录（worktree）。
        lib_name (str)：库名。
    返回值：
        str：包目录绝对路径。
    """
    for cand in (os.path.join(lib_path, lib_name),
                 os.path.join(lib_path, 'lib', lib_name)):
        if os.path.isdir(cand):
            return cand
    return lib_path


def _iter_source_files(pkg_root: str) -> List[str]:
    """遍历包目录下全部 .py / .pyi 文件（跳过 __pycache__ 等编译产物目录）。

    .py 一律排在 .pyi 之前，使同名 API 以 .py 中的定义为准。

    输入参数：
        pkg_root (str)：包目录。
    返回值：
        List[str]：源文件绝对路径列表，.py 在前、.pyi 在后。
    """
    py_files: List[str] = []
    pyi_files: List[str] = []
    for dirpath, dirnames, filenames in os.walk(pkg_root):
        dirnames[:] = [d for d in dirnames
                       if d not in ('__pycache__', '.git', 'build', 'dist')]
        for fname in sorted(filenames):
            if fname.endswith('.py'):
                py_files.append(os.path.join(dirpath, fname))
            elif fname.endswith('.pyi'):
                pyi_files.append(os.path.join(dirpath, fname))
    return py_files + pyi_files


def _module_name(pkg_root: str, src_path: str) -> str:
    """由包目录与源文件路径推出模块路径（如 pandas.core.indexes.multi）。

    保留 __init__ 段：pandas/errors/__init__.py 的模块路径为
    pandas.errors.__init__。

    输入参数：
        pkg_root (str)：包目录，如 <repo>/pandas。
        src_path (str)：该包下的 .py / .pyi 文件绝对路径。
    返回值：
        str：点分模块路径。
    """
    rel = os.path.relpath(src_path, os.path.dirname(pkg_root))
    parts = rel.split(os.sep)
    parts[-1] = os.path.splitext(parts[-1])[0]
    return '.'.join(parts)


# ---------------------------------------------------------------------------
# 版本级提取
# ---------------------------------------------------------------------------

def _resolve_tag(repo_path: str, version: str) -> str:
    """在仓库 tag 序列中查规范化版本号对应的原始 tag。

    输入参数：
        repo_path (str)：库 git 仓库路径。
        version (str)：规范化版本号，如 1.0.0。
    返回值：
        str：原始 tag，如 v1.0.0。
    异常：
        ValueError：该版本不在仓库的稳定版本序列中。
    """
    for v, tag in list_versions(repo_path):
        if v == version:
            return tag
    raise ValueError(f"{repo_path} 中不存在版本 {version}")


def _collect_methods(lib_path: str, pkg_root: str, lib_name: str,
                     version: str) -> Tuple[Dict[str, str], List[str]]:
    """收集一个版本包内全部方法粒度 API。

    .py 先于 .pyi 处理：同一 FQN 在 .py 中已定义时，.pyi 存根不覆盖它。

    输入参数：
        lib_path (str)：版本源码根目录（worktree）。
        pkg_root (str)：包目录。
        lib_name (str)：库名（仅用于日志）。
        version (str)：版本号（仅用于日志）。
    返回值：
        Tuple[Dict[str, str], List[str]]：
            ({方法 FQN: unparse 后的源码文本}, 解析失败文件相对路径列表)；
            解析失败会显式打印并计入返回值，不静默跳过。
    """
    methods: Dict[str, str] = {}
    failed: List[str] = []
    for src_path in _iter_source_files(pkg_root):
        module = _module_name(pkg_root, src_path)
        with open(src_path, encoding='utf-8') as f:
            source = f.read()
        try:
            got = extract_methods_from_source(
                source, module, skip_overload=src_path.endswith('.py'))
        except SyntaxError as e:  # 显式报出并计数，不静默跳过
            rel = os.path.relpath(src_path, lib_path)
            print(f"[WARN] {lib_name} {version} 解析失败 {rel}: {e}",
                  file=sys.stderr, flush=True)
            failed.append(rel)
            continue
        if src_path.endswith('.py'):
            methods.update(got)
        else:
            for fqn, text in got.items():
                methods.setdefault(fqn, text)
    return methods, failed


def _write_candidates(methods: Dict[str, str], out_dir: str,
                      version: str) -> int:
    """把一个版本的方法集合落盘到 candidates/<版本>/，一个方法一个文件。

    输入参数：
        methods (Dict[str, str])：{方法 FQN: 源码文本}。
        out_dir (str)：candidates 输出根目录。
        version (str)：版本号。
    返回值：
        int：写出的方法数。
    """
    ver_dir = os.path.join(out_dir, version)
    os.makedirs(ver_dir, exist_ok=True)
    for fqn, text in methods.items():
        with open(os.path.join(ver_dir, f"{fqn}.py"), 'w',
                  encoding='utf-8') as f:
            f.write(text)
    return len(methods)


def _process_version(lib_name: str, repo_path: str, version: str, tag: str,
                     deprecated_fqn: str, case_dir: str,
                     worktrees_root: Optional[str],
                     do_candidates: bool, do_deprecated: bool) -> Dict:
    """处理单个版本：checkout worktree → 提取 → 清理 worktree。

    供串行与并行（ProcessPoolExecutor）两路复用；git worktree add 在并行下
    偶发锁竞争，故 checkout 失败重试 3 次（线性退避）。

    输入参数：
        lib_name (str)：库名。
        repo_path (str)：库 git 仓库路径。
        version (str)：规范化版本号。
        tag (str)：原始 git tag。
        deprecated_fqn (str)：弃用 API 的源码路径 FQN。
        case_dir (str)：用例目录（candidates/deprecated_api 的父目录）。
        worktrees_root (Optional[str])：worktree 根目录，None 用默认。
        do_candidates (bool)：是否提取候选池。
        do_deprecated (bool)：是否提取弃用 API。
    返回值：
        Dict：{"version", "tag", "n_methods", "n_parse_failed",
               "deprecated_written", "error"}；error 非 None 表示该版本失败。
    """
    # 注：候选池与弃用 API 共用同一次包内方法收集（_collect_methods），
    # 避免为同一版本重复解析整棵源码树。
    dest = worktree_path(lib_name, version, worktrees_root)
    lib_path = None
    last_err: Optional[Exception] = None
    for attempt in range(3):
        try:
            lib_path = checkout_version(repo_path, tag, dest)
            break
        except Exception as e:
            last_err = e
            time.sleep(0.5 * (attempt + 1))

    result = {"version": version, "tag": tag, "n_methods": 0,
              "n_parse_failed": 0, "deprecated_written": False, "error": None}
    try:
        if lib_path is None:
            result["error"] = f"worktree checkout 重试 3 次失败: {last_err}"
            return result
        pkg_root = resolve_package_root(lib_path, lib_name)
        methods, failed = _collect_methods(lib_path, pkg_root, lib_name, version)
        result["n_parse_failed"] = len(failed)
        if do_candidates:
            result["n_methods"] = _write_candidates(
                methods, os.path.join(case_dir, "candidates"), version)
        if do_deprecated:
            result["deprecated_written"] = _extract_deprecated(
                methods, os.path.join(case_dir, "deprecated_api"),
                deprecated_fqn, version)
        return result
    except Exception as e:
        result["error"] = f"{type(e).__name__}: {e}"
        return result
    finally:
        try:
            if os.path.isdir(dest):
                remove_worktree(repo_path, dest)
        except Exception as e:
            print(f"[extract] {lib_name} {version} worktree 清理失败: {e}",
                  file=sys.stderr, flush=True)


def _extract_deprecated(methods: Dict[str, str], out_dir: str,
                        deprecated_fqn: str, version: str) -> bool:
    """提取弃用 API 源码并写到 deprecated_api/<版本>.py。

    按 FQN 的「类名 + 方法名」在版本内的方法集合中匹配，而不是由 FQN 拼接
    源码路径：弃用 API 的所在模块会随版本迁移（例如 pandas 的
    MultiIndex.set_labels 先后位于 pandas/core/index.py、
    pandas/indexes/multi.py、pandas/core/indexes/multi.py）。

    输入参数：
        methods (Dict[str, str])：该版本全部方法，见 _collect_methods。
        out_dir (str)：deprecated_api 输出根目录。
        deprecated_fqn (str)：弃用 API 的 FQN，至少 模块.类.方法 三段。
        version (str)：版本号（用作文件名）。
    返回值：
        bool：写出返回 True；该版本不存在该方法返回 False（不写文件）。
    异常：
        ValueError：FQN 段数不足，或同名方法在该版本存在多处定义时抛出。
    """
    parts = deprecated_fqn.split('.')
    if len(parts) < 3:
        raise ValueError(f"弃用 API FQN 至少需 模块.类.方法 三段: {deprecated_fqn}")
    class_name, method_name = parts[-2], parts[-1]
    matched = [(fqn, text) for fqn, text in methods.items()
               if fqn.rsplit('.', 2)[-2:] == [class_name, method_name]]
    if not matched:
        return False
    if len(matched) > 1:
        raise ValueError(
            f"弃用 API {class_name}.{method_name} 在 {version} 存在多处定义: "
            f"{[fqn for fqn, _ in matched]}，无法确定取哪一个")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f"{version}.py"), 'w',
              encoding='utf-8') as f:
        f.write(matched[0][1])
    return True


# ---------------------------------------------------------------------------
# 入口
# ---------------------------------------------------------------------------

def main(argv=None) -> int:
    """入口：读实验设计 → 逐版本 checkout 并提取 candidates / deprecated_api。

    输入参数：
        argv (Optional[List[str]])：命令行参数；None 用 sys.argv。
    返回值：
        int：0 全部成功；1 存在失败版本。
    """
    parser = argparse.ArgumentParser(
        description="按 experiment.json 提取论文用例的 candidates / deprecated_api")
    parser.add_argument("--case-dir", default=DEFAULT_CASE_DIR, help="用例目录")
    parser.add_argument("--lib", default=DEFAULT_LIB, help="库名（默认 pandas）")
    parser.add_argument("--repo", default=None,
                        help="库 git 仓库路径（默认 <PEAR_ROOT>/Libraries/<lib>）")
    parser.add_argument("--deprecated-fqn", default=None,
                        help="弃用 API FQN（默认由用例目录名解析）")
    parser.add_argument("--versions", default="",
                        help="逗号分隔的版本过滤（空=全部）")
    parser.add_argument("--jobs", type=int, default=1, help="并行进程数（默认 1）")
    parser.add_argument("--worktrees-root", default=None, help="worktree 根目录")
    parser.add_argument("--skip-candidates", action="store_true",
                        help="只提取 deprecated_api")
    parser.add_argument("--skip-deprecated", action="store_true",
                        help="只提取 candidates")
    args = parser.parse_args(argv)

    case_dir = os.path.abspath(args.case_dir)
    repo_path = args.repo or os.path.join(PEAR_ROOT, "Libraries", args.lib)

    experiment = load_experiment(os.path.join(case_dir, "experiment.json"))
    all_cand, all_dep = collect_versions(experiment)
    deprecated_fqn = args.deprecated_fqn or parse_case_name(case_dir)[0]

    cand_versions, dep_versions = all_cand, all_dep
    if args.versions:
        wanted = {v.strip() for v in args.versions.split(",") if v.strip()}
        known = set(all_cand) | set(all_dep)
        unknown = sorted(wanted - known, key=_version_key)
        if unknown:
            raise ValueError(
                f"--versions 中的版本不在 experiment.json 设计范围内: {unknown}；"
                f"可用版本: {sorted(known, key=_version_key)}")
        cand_versions = [v for v in all_cand if v in wanted]
        dep_versions = [v for v in all_dep if v in wanted]

    todo = sorted(set(cand_versions) | set(dep_versions), key=_version_key)
    print(f"用例目录: {case_dir}")
    print(f"仓库: {repo_path}")
    print(f"弃用 API: {deprecated_fqn}")
    print(f"待处理版本 {len(todo)} 个: {', '.join(todo)}")
    print(f"  candidates 版本 {len(cand_versions)} 个（--skip-candidates="
          f"{args.skip_candidates}）")
    print(f"  deprecated 版本 {len(dep_versions)} 个（--skip-deprecated="
          f"{args.skip_deprecated}）")

    tasks = []
    for version in todo:
        tag = _resolve_tag(repo_path, version)
        tasks.append((version, tag,
                      version in cand_versions and not args.skip_candidates,
                      version in dep_versions and not args.skip_deprecated))

    results: List[Dict] = []
    if args.jobs > 1:
        with ProcessPoolExecutor(max_workers=args.jobs) as ex:
            futures = [
                ex.submit(_process_version, args.lib, repo_path, v, tag,
                          deprecated_fqn, case_dir, args.worktrees_root,
                          do_cand, do_dep)
                for v, tag, do_cand, do_dep in tasks]
            for fut in as_completed(futures):
                r = fut.result()
                results.append(r)
                _report(r)
    else:
        for v, tag, do_cand, do_dep in tasks:
            r = _process_version(args.lib, repo_path, v, tag, deprecated_fqn,
                                 case_dir, args.worktrees_root, do_cand, do_dep)
            results.append(r)
            _report(r)

    failed = [r for r in results if r["error"]]
    print(f"\n完成: {len(results)} 个版本 / 失败 {len(failed)}")
    for r in failed:
        print(f"  - {r['version']} (tag={r['tag']}): {r['error']}")
    return 1 if failed else 0


def _report(result: Dict) -> None:
    """打印单版本提取结果。"""
    if result["error"]:
        print(f"[FAIL] {result['version']}: {result['error']}", flush=True)
        return
    print(f"[ok] {result['version']}: 方法 {result['n_methods']} 个"
          f"（解析失败 {result['n_parse_failed']} 个文件）"
          f"{'，已写 deprecated_api' if result['deprecated_written'] else ''}",
          flush=True)


if __name__ == "__main__":
    sys.exit(main())
