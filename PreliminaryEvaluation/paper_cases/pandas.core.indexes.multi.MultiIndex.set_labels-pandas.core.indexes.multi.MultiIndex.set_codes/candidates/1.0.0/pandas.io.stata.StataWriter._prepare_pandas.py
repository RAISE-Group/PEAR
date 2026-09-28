def _prepare_pandas(self, data):
    data = data.copy()
    if self._write_index:
        data = data.reset_index()
    data = self._check_column_names(data)
    data = _cast_to_stata_types(data)
    data = self._replace_nans(data)
    data = self._prepare_categoricals(data)
    self.nobs, self.nvar = data.shape
    self.data = data
    self.varlist = data.columns.tolist()
    dtypes = data.dtypes
    for col in data:
        if col in self._convert_dates:
            continue
        if is_datetime64_dtype(data[col]):
            self._convert_dates[col] = 'tc'
    self._convert_dates = _maybe_convert_to_int_keys(self._convert_dates, self.varlist)
    for key in self._convert_dates:
        new_type = _convert_datetime_to_stata_type(self._convert_dates[key])
        dtypes[key] = np.dtype(new_type)
    self._encode_strings()
    self._set_formats_and_types(dtypes)
    if self._convert_dates is not None:
        for key in self._convert_dates:
            self.fmtlist[key] = self._convert_dates[key]