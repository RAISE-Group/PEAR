def _choose_path(self, fast_path: Callable, slow_path: Callable, group: DataFrame):
    path = slow_path
    res = slow_path(group)
    try:
        res_fast = fast_path(group)
    except AssertionError:
        raise
    except Exception:
        return (path, res)
    if not isinstance(res_fast, DataFrame):
        return (path, res)
    if not res_fast.columns.equals(group.columns):
        return (path, res)
    if res_fast.equals(res):
        path = fast_path
    return (path, res)