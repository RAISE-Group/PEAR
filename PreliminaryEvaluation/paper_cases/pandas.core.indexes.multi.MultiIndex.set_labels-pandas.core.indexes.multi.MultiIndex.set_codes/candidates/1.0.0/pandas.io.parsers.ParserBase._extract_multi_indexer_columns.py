def _extract_multi_indexer_columns(self, header, index_names, col_names, passed_names=False):
    """ extract and return the names, index_names, col_names
            header is a list-of-lists returned from the parsers """
    if len(header) < 2:
        return (header[0], index_names, col_names, passed_names)
    ic = self.index_col
    if ic is None:
        ic = []
    if not isinstance(ic, (list, tuple, np.ndarray)):
        ic = [ic]
    sic = set(ic)
    index_names = header.pop(-1)
    index_names, names, index_col = _clean_index_names(index_names, self.index_col, self.unnamed_cols)
    field_count = len(header[0])

    def extract(r):
        return tuple((r[i] for i in range(field_count) if i not in sic))
    columns = list(zip(*(extract(r) for r in header)))
    names = ic + columns
    for n in range(len(columns[0])):
        if all((ensure_str(col[n]) in self.unnamed_cols for col in columns)):
            raise ParserError('Passed header=[{header}] are too many rows for this multi_index of columns'.format(header=','.join((str(x) for x in self.header))))
    if len(ic):
        col_names = [r[0] if len(r[0]) and r[0] not in self.unnamed_cols else None for r in header]
    else:
        col_names = [None] * len(header)
    passed_names = True
    return (names, index_names, col_names, passed_names)