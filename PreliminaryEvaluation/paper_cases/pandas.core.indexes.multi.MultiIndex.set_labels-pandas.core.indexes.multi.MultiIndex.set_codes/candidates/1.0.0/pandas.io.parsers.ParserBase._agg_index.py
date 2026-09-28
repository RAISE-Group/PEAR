def _agg_index(self, index, try_parse_dates=True):
    arrays = []
    for i, arr in enumerate(index):
        if try_parse_dates and self._should_parse_dates(i):
            arr = self._date_conv(arr)
        if self.na_filter:
            col_na_values = self.na_values
            col_na_fvalues = self.na_fvalues
        else:
            col_na_values = set()
            col_na_fvalues = set()
        if isinstance(self.na_values, dict):
            col_name = self.index_names[i]
            if col_name is not None:
                col_na_values, col_na_fvalues = _get_na_values(col_name, self.na_values, self.na_fvalues, self.keep_default_na)
        arr, _ = self._infer_types(arr, col_na_values | col_na_fvalues)
        arrays.append(arr)
    names = self.index_names
    index = ensure_index_from_sequences(arrays, names)
    return index