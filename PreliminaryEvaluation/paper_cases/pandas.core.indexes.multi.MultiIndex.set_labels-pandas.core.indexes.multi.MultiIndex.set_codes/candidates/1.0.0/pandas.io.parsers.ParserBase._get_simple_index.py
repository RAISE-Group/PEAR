def _get_simple_index(self, data, columns):

    def ix(col):
        if not isinstance(col, str):
            return col
        raise ValueError(f'Index {col} invalid')
    to_remove = []
    index = []
    for idx in self.index_col:
        i = ix(idx)
        to_remove.append(i)
        index.append(data[i])
    for i in sorted(to_remove, reverse=True):
        data.pop(i)
        if not self._implicit_index:
            columns.pop(i)
    return index