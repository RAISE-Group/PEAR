def _reduce(self, method, skipna=True, **kwargs):
    if skipna:
        arr = self[~self.isna()]
    else:
        arr = self
    try:
        op = getattr(arr, method)
    except AttributeError:
        raise TypeError
    return op(**kwargs)