def _infer_columns(self):
    names = self.names
    num_original_columns = 0
    clear_buffer = True
    unnamed_cols = set()
    if self.header is not None:
        header = self.header
        if isinstance(header, (list, tuple, np.ndarray)):
            have_mi_columns = len(header) > 1
            if have_mi_columns:
                header = list(header) + [header[-1] + 1]
        else:
            have_mi_columns = False
            header = [header]
        columns = []
        for level, hr in enumerate(header):
            try:
                line = self._buffered_line()
                while self.line_pos <= hr:
                    line = self._next_line()
            except StopIteration:
                if self.line_pos < hr:
                    raise ValueError(f'Passed header={hr} but only {self.line_pos + 1} lines in file')
                if have_mi_columns and hr > 0:
                    if clear_buffer:
                        self._clear_buffer()
                    columns.append([None] * len(columns[-1]))
                    return (columns, num_original_columns, unnamed_cols)
                if not self.names:
                    raise EmptyDataError('No columns to parse from file')
                line = self.names[:]
            this_columns = []
            this_unnamed_cols = []
            for i, c in enumerate(line):
                if c == '':
                    if have_mi_columns:
                        col_name = f'Unnamed: {i}_level_{level}'
                    else:
                        col_name = f'Unnamed: {i}'
                    this_unnamed_cols.append(i)
                    this_columns.append(col_name)
                else:
                    this_columns.append(c)
            if not have_mi_columns and self.mangle_dupe_cols:
                counts = defaultdict(int)
                for i, col in enumerate(this_columns):
                    cur_count = counts[col]
                    while cur_count > 0:
                        counts[col] = cur_count + 1
                        col = f'{col}.{cur_count}'
                        cur_count = counts[col]
                    this_columns[i] = col
                    counts[col] = cur_count + 1
            elif have_mi_columns:
                if hr == header[-1]:
                    lc = len(this_columns)
                    ic = len(self.index_col) if self.index_col is not None else 0
                    unnamed_count = len(this_unnamed_cols)
                    if lc != unnamed_count and lc - ic > unnamed_count:
                        clear_buffer = False
                        this_columns = [None] * lc
                        self.buf = [self.buf[-1]]
            columns.append(this_columns)
            unnamed_cols.update({this_columns[i] for i in this_unnamed_cols})
            if len(columns) == 1:
                num_original_columns = len(this_columns)
        if clear_buffer:
            self._clear_buffer()
        if names is not None:
            if self.usecols is not None and len(names) != len(self.usecols) or (self.usecols is None and len(names) != len(columns[0])):
                raise ValueError('Number of passed names did not match number of header fields in the file')
            if len(columns) > 1:
                raise TypeError('Cannot pass names with multi-index columns')
            if self.usecols is not None:
                self._handle_usecols(columns, names)
            else:
                self._col_indices = None
                num_original_columns = len(names)
            columns = [names]
        else:
            columns = self._handle_usecols(columns, columns[0])
    else:
        try:
            line = self._buffered_line()
        except StopIteration:
            if not names:
                raise EmptyDataError('No columns to parse from file')
            line = names[:]
        ncols = len(line)
        num_original_columns = ncols
        if not names:
            if self.prefix:
                columns = [[f'{self.prefix}{i}' for i in range(ncols)]]
            else:
                columns = [list(range(ncols))]
            columns = self._handle_usecols(columns, columns[0])
        elif self.usecols is None or len(names) >= num_original_columns:
            columns = self._handle_usecols([names], names)
            num_original_columns = len(names)
        else:
            if not callable(self.usecols) and len(names) != len(self.usecols):
                raise ValueError('Number of passed names did not match number of header fields in the file')
            self._handle_usecols([names], names)
            columns = [names]
            num_original_columns = ncols
    return (columns, num_original_columns, unnamed_cols)