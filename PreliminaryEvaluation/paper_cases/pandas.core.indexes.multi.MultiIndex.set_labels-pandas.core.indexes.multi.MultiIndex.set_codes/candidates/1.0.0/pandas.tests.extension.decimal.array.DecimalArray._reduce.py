def _reduce(self, name, skipna=True, **kwargs):
    if skipna:
        if self.isna().any():
            other = self[~self.isna()]
            return other._reduce(name, **kwargs)
    if name == 'sum' and len(self) == 0:
        return decimal.Decimal(0)
    try:
        op = getattr(self.data, name)
    except AttributeError:
        raise NotImplementedError(f'decimal does not support the {name} operation')
    return op(axis=0)