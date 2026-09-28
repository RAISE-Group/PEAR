def _reduce(self, name, skipna=True, **kwargs):
    if name in {'any', 'all'}:
        return getattr(self, name)(skipna=skipna, **kwargs)
    data = self._data
    mask = self._mask
    if self._hasna:
        data = self.to_numpy('float64', na_value=np.nan)
    op = getattr(nanops, 'nan' + name)
    result = op(data, axis=0, skipna=skipna, mask=mask, **kwargs)
    if np.isnan(result):
        return libmissing.NA
    if name in ['sum', 'prod'] and notna(result):
        int_result = np.int64(result)
        if int_result == result:
            result = int_result
    elif name in ['min', 'max'] and notna(result):
        result = np.bool_(result)
    return result