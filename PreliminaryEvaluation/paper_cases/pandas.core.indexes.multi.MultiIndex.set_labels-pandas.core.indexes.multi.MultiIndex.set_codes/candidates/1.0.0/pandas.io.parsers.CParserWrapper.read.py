def read(self, nrows=None):
    try:
        data = self._reader.read(nrows)
    except StopIteration:
        if self._first_chunk:
            self._first_chunk = False
            names = self._maybe_dedup_names(self.orig_names)
            index, columns, col_dict = _get_empty_meta(names, self.index_col, self.index_names, dtype=self.kwds.get('dtype'))
            columns = self._maybe_make_multi_index_columns(columns, self.col_names)
            if self.usecols is not None:
                columns = self._filter_usecols(columns)
            col_dict = dict(filter(lambda item: item[0] in columns, col_dict.items()))
            return (index, columns, col_dict)
        else:
            raise
    self._first_chunk = False
    names = self.names
    if self._reader.leading_cols:
        if self._has_complex_date_col:
            raise NotImplementedError('file structure not yet supported')
        arrays = []
        for i in range(self._reader.leading_cols):
            if self.index_col is None:
                values = data.pop(i)
            else:
                values = data.pop(self.index_col[i])
            values = self._maybe_parse_dates(values, i, try_parse_dates=True)
            arrays.append(values)
        index = ensure_index_from_sequences(arrays)
        if self.usecols is not None:
            names = self._filter_usecols(names)
        names = self._maybe_dedup_names(names)
        data = sorted(data.items())
        data = {k: v for k, (i, v) in zip(names, data)}
        names, data = self._do_date_conversions(names, data)
    else:
        data = sorted(data.items())
        names = list(self.orig_names)
        names = self._maybe_dedup_names(names)
        if self.usecols is not None:
            names = self._filter_usecols(names)
        alldata = [x[1] for x in data]
        data = {k: v for k, (i, v) in zip(names, data)}
        names, data = self._do_date_conversions(names, data)
        index, names = self._make_index(data, alldata, names)
    names = self._maybe_make_multi_index_columns(names, self.col_names)
    return (index, names, data)