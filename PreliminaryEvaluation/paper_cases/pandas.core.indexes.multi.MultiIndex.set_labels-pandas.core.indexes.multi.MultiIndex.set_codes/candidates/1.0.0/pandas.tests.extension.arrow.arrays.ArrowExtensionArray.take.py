def take(self, indices, allow_fill=False, fill_value=None):
    data = self._data.to_pandas()
    if allow_fill and fill_value is None:
        fill_value = self.dtype.na_value
    result = take(data, indices, fill_value=fill_value, allow_fill=allow_fill)
    return self._from_sequence(result, dtype=self.dtype)