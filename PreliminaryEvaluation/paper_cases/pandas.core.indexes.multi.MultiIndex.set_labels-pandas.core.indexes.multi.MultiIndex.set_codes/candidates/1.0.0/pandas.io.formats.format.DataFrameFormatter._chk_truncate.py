def _chk_truncate(self) -> None:
    """
        Checks whether the frame should be truncated. If so, slices
        the frame up.
        """
    from pandas.core.reshape.concat import concat
    max_cols = self.max_cols
    max_rows = self.max_rows
    self.max_rows_adj: Optional[int]
    max_rows_adj: Optional[int]
    if max_cols == 0 or max_rows == 0:
        w, h = get_terminal_size()
        self.w = w
        self.h = h
        if self.max_rows == 0:
            dot_row = 1
            prompt_row = 1
            if self.show_dimensions:
                show_dimension_rows = 3
            self.header = cast(bool, self.header)
            n_add_rows = self.header + dot_row + show_dimension_rows + prompt_row
            max_rows_adj = self.h - n_add_rows
            self.max_rows_adj = max_rows_adj
        if max_cols == 0 and len(self.frame.columns) > w:
            max_cols = w
        if max_rows == 0 and len(self.frame) > h:
            max_rows = h
    if not hasattr(self, 'max_rows_adj'):
        if max_rows:
            if len(self.frame) > max_rows and self.min_rows:
                max_rows = min(self.min_rows, max_rows)
        self.max_rows_adj = max_rows
    if not hasattr(self, 'max_cols_adj'):
        self.max_cols_adj = max_cols
    max_cols_adj = self.max_cols_adj
    max_rows_adj = self.max_rows_adj
    truncate_h = max_cols_adj and len(self.columns) > max_cols_adj
    truncate_v = max_rows_adj and len(self.frame) > max_rows_adj
    frame = self.frame
    if truncate_h:
        max_cols_adj = cast(int, max_cols_adj)
        if max_cols_adj == 0:
            col_num = len(frame.columns)
        elif max_cols_adj == 1:
            max_cols = cast(int, max_cols)
            frame = frame.iloc[:, :max_cols]
            col_num = max_cols
        else:
            col_num = max_cols_adj // 2
            frame = concat((frame.iloc[:, :col_num], frame.iloc[:, -col_num:]), axis=1)
            if isinstance(self.formatters, (list, tuple)):
                truncate_fmt = self.formatters
                self.formatters = [*truncate_fmt[:col_num], *truncate_fmt[-col_num:]]
        self.tr_col_num = col_num
    if truncate_v:
        max_rows_adj = cast(int, max_rows_adj)
        if max_rows_adj == 1:
            row_num = max_rows
            frame = frame.iloc[:max_rows, :]
        else:
            row_num = max_rows_adj // 2
            frame = concat((frame.iloc[:row_num, :], frame.iloc[-row_num:, :]))
        self.tr_row_num = row_num
    else:
        self.tr_row_num = None
    self.tr_frame = frame
    self.truncate_h = truncate_h
    self.truncate_v = truncate_v
    self.is_truncated = bool(self.truncate_h or self.truncate_v)