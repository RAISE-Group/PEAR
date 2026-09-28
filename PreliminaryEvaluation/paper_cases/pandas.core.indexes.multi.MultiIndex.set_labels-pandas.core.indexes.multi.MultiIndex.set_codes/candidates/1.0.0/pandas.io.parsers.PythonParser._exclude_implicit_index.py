def _exclude_implicit_index(self, alldata):
    names = self._maybe_dedup_names(self.orig_names)
    if self._implicit_index:
        excl_indices = self.index_col
        data = {}
        offset = 0
        for i, col in enumerate(names):
            while i + offset in excl_indices:
                offset += 1
            data[col] = alldata[i + offset]
    else:
        data = {k: v for k, v in zip(names, alldata)}
    return data