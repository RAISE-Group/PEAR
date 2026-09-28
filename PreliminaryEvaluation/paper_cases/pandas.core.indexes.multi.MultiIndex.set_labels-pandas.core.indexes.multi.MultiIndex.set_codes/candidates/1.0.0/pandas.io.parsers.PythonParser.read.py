def read(self, rows=None):
    try:
        content = self._get_lines(rows)
    except StopIteration:
        if self._first_chunk:
            content = []
        else:
            raise
    self._first_chunk = False
    columns = list(self.orig_names)
    if not len(content):
        names = self._maybe_dedup_names(self.orig_names)
        index, columns, col_dict = _get_empty_meta(names, self.index_col, self.index_names, self.dtype)
        columns = self._maybe_make_multi_index_columns(columns, self.col_names)
        return (index, columns, col_dict)
    count_empty_content_vals = count_empty_vals(content[0])
    indexnamerow = None
    if self.has_index_names and count_empty_content_vals == len(columns):
        indexnamerow = content[0]
        content = content[1:]
    alldata = self._rows_to_cols(content)
    data = self._exclude_implicit_index(alldata)
    columns = self._maybe_dedup_names(self.columns)
    columns, data = self._do_date_conversions(columns, data)
    data = self._convert_data(data)
    index, columns = self._make_index(data, alldata, columns, indexnamerow)
    return (index, columns, data)