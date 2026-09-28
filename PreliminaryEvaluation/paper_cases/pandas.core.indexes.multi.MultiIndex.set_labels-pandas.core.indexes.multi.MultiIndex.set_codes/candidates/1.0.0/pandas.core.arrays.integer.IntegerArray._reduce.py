def _reduce(self, name, skipna=True, **kwargs):
    data = self._data
    mask = self._mask
    if self._hasna:
        data = self.to_numpy('float64', na_value=np.nan)
    op = getattr(nanops, 'nan' + name)
    result = op(data, axis=0, skipna=skipna, mask=mask, **kwargs)
    if np.isnan(result):
        return libmissing.NA
    if name in ['any', 'all']:
        pass
    elif name in ['sum', 'min', 'max', 'prod']:
        int_result = int(result)
        if int_result == result:
            result = int_result
    return result