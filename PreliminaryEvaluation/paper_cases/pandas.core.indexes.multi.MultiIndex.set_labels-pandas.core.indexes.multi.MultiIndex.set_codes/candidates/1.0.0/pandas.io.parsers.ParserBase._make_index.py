def _make_index(self, data, alldata, columns, indexnamerow=False):
    if not _is_index_col(self.index_col) or not self.index_col:
        index = None
    elif not self._has_complex_date_col:
        index = self._get_simple_index(alldata, columns)
        index = self._agg_index(index)
    elif self._has_complex_date_col:
        if not self._name_processed:
            self.index_names, _, self.index_col = _clean_index_names(list(columns), self.index_col, self.unnamed_cols)
            self._name_processed = True
        index = self._get_complex_date_index(data, columns)
        index = self._agg_index(index, try_parse_dates=False)
    if indexnamerow:
        coffset = len(indexnamerow) - len(columns)
        index = index.set_names(indexnamerow[:coffset])
    columns = self._maybe_make_multi_index_columns(columns, self.col_names)
    return (index, columns)