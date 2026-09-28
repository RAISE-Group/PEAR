def _to_str_columns(self) -> List[List[str]]:
    """
        Render a DataFrame to a list of columns (as lists of strings).
        """
    self.col_space = cast(int, self.col_space)
    frame = self.tr_frame
    str_index = self._get_formatted_index(frame)
    if not is_list_like(self.header) and (not self.header):
        stringified = []
        for i, c in enumerate(frame):
            fmt_values = self._format_col(i)
            fmt_values = _make_fixed_width(fmt_values, self.justify, minimum=self.col_space or 0, adj=self.adj)
            stringified.append(fmt_values)
    else:
        if is_list_like(self.header):
            self.header = cast(List[str], self.header)
            if len(self.header) != len(self.columns):
                raise ValueError('Writing {ncols} cols but got {nalias} aliases'.format(ncols=len(self.columns), nalias=len(self.header)))
            str_columns = [[label] for label in self.header]
        else:
            str_columns = self._get_formatted_column_labels(frame)
        if self.show_row_idx_names:
            for x in str_columns:
                x.append('')
        stringified = []
        for i, c in enumerate(frame):
            cheader = str_columns[i]
            header_colwidth = max(self.col_space or 0, *(self.adj.len(x) for x in cheader))
            fmt_values = self._format_col(i)
            fmt_values = _make_fixed_width(fmt_values, self.justify, minimum=header_colwidth, adj=self.adj)
            max_len = max(max((self.adj.len(x) for x in fmt_values)), header_colwidth)
            cheader = self.adj.justify(cheader, max_len, mode=self.justify)
            stringified.append(cheader + fmt_values)
    strcols = stringified
    if self.index:
        strcols.insert(0, str_index)
    truncate_h = self.truncate_h
    truncate_v = self.truncate_v
    if truncate_h:
        col_num = self.tr_col_num
        strcols.insert(self.tr_col_num + 1, [' ...'] * len(str_index))
    if truncate_v:
        n_header_rows = len(str_index) - len(frame)
        row_num = self.tr_row_num
        row_num = cast(int, row_num)
        for ix, col in enumerate(strcols):
            cwidth = self.adj.len(strcols[ix][row_num])
            is_dot_col = False
            if truncate_h:
                is_dot_col = ix == col_num + 1
            if cwidth > 3 or is_dot_col:
                my_str = '...'
            else:
                my_str = '..'
            if ix == 0:
                dot_mode = 'left'
            elif is_dot_col:
                cwidth = 4
                dot_mode = 'right'
            else:
                dot_mode = 'right'
            dot_str = self.adj.justify([my_str], cwidth, mode=dot_mode)[0]
            strcols[ix].insert(row_num + n_header_rows, dot_str)
    return strcols