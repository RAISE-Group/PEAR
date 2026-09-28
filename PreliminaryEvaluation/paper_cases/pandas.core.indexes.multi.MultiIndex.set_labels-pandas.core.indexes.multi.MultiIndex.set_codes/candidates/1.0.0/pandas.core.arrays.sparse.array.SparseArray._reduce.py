def _reduce(self, name, skipna=True, **kwargs):
    method = getattr(self, name, None)
    if method is None:
        raise TypeError(f'cannot perform {name} with type {self.dtype}')
    if skipna:
        arr = self
    else:
        arr = self.dropna()
    kwargs.pop('filter_type', None)
    kwargs.pop('numeric_only', None)
    kwargs.pop('op', None)
    return getattr(arr, name)(**kwargs)