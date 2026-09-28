def read(self, nrows=None):
    nrows = _validate_integer('nrows', nrows)
    ret = self._engine.read(nrows)
    index, columns, col_dict = self._create_index(ret)
    if index is None:
        if col_dict:
            new_rows = len(next(iter(col_dict.values())))
            index = RangeIndex(self._currow, self._currow + new_rows)
        else:
            new_rows = 0
    else:
        new_rows = len(index)
    df = DataFrame(col_dict, columns=columns, index=index)
    self._currow += new_rows
    if self.squeeze and len(df.columns) == 1:
        return df[df.columns[0]].copy()
    return df