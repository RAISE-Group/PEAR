def _parse_no_numpy(self):
    data = loads(self.json, precise_float=self.precise_float)
    if self.orient == 'split':
        decoded = {str(k): v for k, v in data.items()}
        self.check_keys_split(decoded)
        self.obj = create_series_with_explicit_dtype(**decoded)
    else:
        self.obj = create_series_with_explicit_dtype(data, dtype_if_empty=object)