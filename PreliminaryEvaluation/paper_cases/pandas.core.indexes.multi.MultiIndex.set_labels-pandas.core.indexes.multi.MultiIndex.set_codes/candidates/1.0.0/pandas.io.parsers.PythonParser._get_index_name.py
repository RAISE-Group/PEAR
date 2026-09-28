def _get_index_name(self, columns):
    """
        Try several cases to get lines:

        0) There are headers on row 0 and row 1 and their
        total summed lengths equals the length of the next line.
        Treat row 0 as columns and row 1 as indices
        1) Look for implicit index: there are more columns
        on row 1 than row 0. If this is true, assume that row
        1 lists index columns and row 0 lists normal columns.
        2) Get index from the columns if it was listed.
        """
    orig_names = list(columns)
    columns = list(columns)
    try:
        line = self._next_line()
    except StopIteration:
        line = None
    try:
        next_line = self._next_line()
    except StopIteration:
        next_line = None
    implicit_first_cols = 0
    if line is not None:
        if self.index_col is not False:
            implicit_first_cols = len(line) - self.num_original_columns
        if next_line is not None:
            if len(next_line) == len(line) + self.num_original_columns:
                self.index_col = list(range(len(line)))
                self.buf = self.buf[1:]
                for c in reversed(line):
                    columns.insert(0, c)
                orig_names = list(columns)
                self.num_original_columns = len(columns)
                return (line, orig_names, columns)
    if implicit_first_cols > 0:
        self._implicit_index = True
        if self.index_col is None:
            self.index_col = list(range(implicit_first_cols))
        index_name = None
    else:
        index_name, columns_, self.index_col = _clean_index_names(columns, self.index_col, self.unnamed_cols)
    return (index_name, orig_names, columns)