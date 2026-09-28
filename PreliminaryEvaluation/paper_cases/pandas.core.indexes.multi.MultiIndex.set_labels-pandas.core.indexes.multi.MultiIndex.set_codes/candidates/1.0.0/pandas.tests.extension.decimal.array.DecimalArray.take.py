def take(self, indexer, allow_fill=False, fill_value=None):
    from pandas.api.extensions import take
    data = self._data
    if allow_fill and fill_value is None:
        fill_value = self.dtype.na_value
    result = take(data, indexer, fill_value=fill_value, allow_fill=allow_fill)
    return self._from_sequence(result)