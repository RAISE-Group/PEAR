def take(self, indexer, allow_fill=False, fill_value=None):
    data_fill_value = self._internal_fill_value if isna(fill_value) else fill_value
    result = take(self._data, indexer, fill_value=data_fill_value, allow_fill=allow_fill)
    mask = take(self._mask, indexer, fill_value=True, allow_fill=allow_fill)
    if allow_fill and notna(fill_value):
        fill_mask = np.asarray(indexer) == -1
        result[fill_mask] = fill_value
        mask = mask ^ fill_mask
    return type(self)(result, mask, copy=False)