def fillna(self, value=None, method=None, limit=None):
    value, method = validate_fillna_kwargs(value, method)
    mask = self.isna()
    if is_array_like(value):
        if len(value) != len(self):
            raise ValueError(f"Length of 'value' does not match. Got ({len(value)})  expected {len(self)}")
        value = value[mask]
    if mask.any():
        if method is not None:
            func = pad_1d if method == 'pad' else backfill_1d
            new_values = func(self._ndarray, limit=limit, mask=mask)
            new_values = self._from_sequence(new_values, dtype=self.dtype)
        else:
            new_values = self.copy()
            new_values[mask] = value
    else:
        new_values = self.copy()
    return new_values