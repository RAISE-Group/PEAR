def _get_index_names(self):
    names = list(self._reader.header[0])
    idx_names = None
    if self._reader.leading_cols == 0 and self.index_col is not None:
        idx_names, names, self.index_col = _clean_index_names(names, self.index_col, self.unnamed_cols)
    return (names, idx_names)