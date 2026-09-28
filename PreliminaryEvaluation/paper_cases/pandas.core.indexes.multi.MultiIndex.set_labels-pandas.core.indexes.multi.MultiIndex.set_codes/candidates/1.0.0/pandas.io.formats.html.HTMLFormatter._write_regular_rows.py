def _write_regular_rows(self, fmt_values: Mapping[int, List[str]], indent: int) -> None:
    truncate_h = self.fmt.truncate_h
    truncate_v = self.fmt.truncate_v
    nrows = len(self.fmt.tr_frame)
    if self.fmt.index:
        fmt = self.fmt._get_formatter('__index__')
        if fmt is not None:
            index_values = self.fmt.tr_frame.index.map(fmt)
        else:
            index_values = self.fmt.tr_frame.index.format()
    row: List[str] = []
    for i in range(nrows):
        if truncate_v and i == self.fmt.tr_row_num:
            str_sep_row = ['...'] * len(row)
            self.write_tr(str_sep_row, indent, self.indent_delta, tags=None, nindex_levels=self.row_levels)
        row = []
        if self.fmt.index:
            row.append(index_values[i])
        elif self.show_col_idx_names:
            row.append('')
        row.extend((fmt_values[j][i] for j in range(self.ncols)))
        if truncate_h:
            dot_col_ix = self.fmt.tr_col_num + self.row_levels
            row.insert(dot_col_ix, '...')
        self.write_tr(row, indent, self.indent_delta, tags=None, nindex_levels=self.row_levels)