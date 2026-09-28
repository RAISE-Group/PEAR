def delete(self, where=None, start: Optional[int]=None, stop: Optional[int]=None):
    if where is None or not len(where):
        if start is None and stop is None:
            nrows = self.nrows
            self._handle.remove_node(self.group, recursive=True)
        else:
            if stop is None:
                stop = self.nrows
            nrows = self.table.remove_rows(start=start, stop=stop)
            self.table.flush()
        return nrows
    if not self.infer_axes():
        return None
    table = self.table
    selection = Selection(self, where, start=start, stop=stop)
    values = selection.select_coords()
    sorted_series = Series(values).sort_values()
    ln = len(sorted_series)
    if ln:
        diff = sorted_series.diff()
        groups = list(diff[diff > 1].index)
        if not len(groups):
            groups = [0]
        if groups[-1] != ln:
            groups.append(ln)
        if groups[0] != 0:
            groups.insert(0, 0)
        pg = groups.pop()
        for g in reversed(groups):
            rows = sorted_series.take(range(g, pg))
            table.remove_rows(start=rows[rows.index[0]], stop=rows[rows.index[-1]] + 1)
            pg = g
        self.table.flush()
    return ln