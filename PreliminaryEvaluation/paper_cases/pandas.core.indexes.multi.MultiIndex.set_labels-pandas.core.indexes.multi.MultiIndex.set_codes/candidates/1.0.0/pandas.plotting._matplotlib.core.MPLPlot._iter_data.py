def _iter_data(self, data=None, keep_index=False, fillna=None):
    if data is None:
        data = self.data
    if fillna is not None:
        data = data.fillna(fillna)
    for col, values in data.items():
        if keep_index is True:
            yield (col, values)
        else:
            yield (col, values.values)