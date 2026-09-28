def _get_complex_date_index(self, data, col_names):

    def _get_name(icol):
        if isinstance(icol, str):
            return icol
        if col_names is None:
            raise ValueError(f'Must supply column order to use {icol!s} as index')
        for i, c in enumerate(col_names):
            if i == icol:
                return c
    to_remove = []
    index = []
    for idx in self.index_col:
        name = _get_name(idx)
        to_remove.append(name)
        index.append(data[name])
    for c in sorted(to_remove, reverse=True):
        data.pop(c)
        col_names.remove(c)
    return index