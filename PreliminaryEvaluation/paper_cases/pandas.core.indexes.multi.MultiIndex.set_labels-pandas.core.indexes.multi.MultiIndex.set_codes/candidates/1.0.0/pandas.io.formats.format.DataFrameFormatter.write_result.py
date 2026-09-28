def write_result(self, buf: IO[str]) -> None:
    """
        Render a DataFrame to a console-friendly tabular output.
        """
    from pandas import Series
    frame = self.frame
    if len(frame.columns) == 0 or len(frame.index) == 0:
        info_line = 'Empty {name}\nColumns: {col}\nIndex: {idx}'.format(name=type(self.frame).__name__, col=pprint_thing(frame.columns), idx=pprint_thing(frame.index))
        text = info_line
    else:
        strcols = self._to_str_columns()
        if self.line_width is None:
            text = self.adj.adjoin(1, *strcols)
        elif not isinstance(self.max_cols, int) or self.max_cols > 0:
            text = self._join_multiline(*strcols)
        else:
            lines = self.adj.adjoin(1, *strcols).split('\n')
            max_len = Series(lines).str.len().max()
            dif = max_len - self.w
            adj_dif = dif + 1
            col_lens = Series([Series(ele).apply(len).max() for ele in strcols])
            n_cols = len(col_lens)
            counter = 0
            while adj_dif > 0 and n_cols > 1:
                counter += 1
                mid = int(round(n_cols / 2.0))
                mid_ix = col_lens.index[mid]
                col_len = col_lens[mid_ix]
                adj_dif -= col_len + 1
                col_lens = col_lens.drop(mid_ix)
                n_cols = len(col_lens)
            max_cols_adj = n_cols - self.index
            max_cols_adj = max(max_cols_adj, 2)
            self.max_cols_adj = max_cols_adj
            self._chk_truncate()
            strcols = self._to_str_columns()
            text = self.adj.adjoin(1, *strcols)
    buf.writelines(text)
    if self.should_show_dimensions:
        buf.write('\n\n[{nrows} rows x {ncols} columns]'.format(nrows=len(frame), ncols=len(frame.columns)))