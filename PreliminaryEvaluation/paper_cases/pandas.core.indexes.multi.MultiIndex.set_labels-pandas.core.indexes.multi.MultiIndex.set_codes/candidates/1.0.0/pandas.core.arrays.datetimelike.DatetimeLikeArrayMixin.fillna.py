def fillna(self, value=None, method=None, limit=None):
    if isinstance(value, ABCSeries):
        value = value.array
    value, method = validate_fillna_kwargs(value, method)
    mask = self.isna()
    if is_array_like(value):
        if len(value) != len(self):
            raise ValueError(f"Length of 'value' does not match. Got ({len(value)})  expected {len(self)}")
        value = value[mask]
    if mask.any():
        if method is not None:
            if method == 'pad':
                func = missing.pad_1d
            else:
                func = missing.backfill_1d
            values = self._data
            if not is_period_dtype(self):
                values = values.copy()
            new_values = func(values, limit=limit, mask=mask)
            if is_datetime64tz_dtype(self):
                new_values = new_values.view('i8')
            new_values = type(self)(new_values, dtype=self.dtype)
        else:
            new_values = self.copy()
            new_values[mask] = value
    else:
        new_values = self.copy()
    return new_values