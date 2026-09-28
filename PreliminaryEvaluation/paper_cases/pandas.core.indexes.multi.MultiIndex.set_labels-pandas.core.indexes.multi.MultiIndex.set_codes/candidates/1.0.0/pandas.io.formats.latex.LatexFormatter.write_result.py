def write_result(self, buf: IO[str]) -> None:
    """
        Render a DataFrame to a LaTeX tabular, longtable, or table/tabular
        environment output.
        """
    if len(self.frame.columns) == 0 or len(self.frame.index) == 0:
        info_line = 'Empty {name}\nColumns: {col}\nIndex: {idx}'.format(name=type(self.frame).__name__, col=self.frame.columns, idx=self.frame.index)
        strcols = [[info_line]]
    else:
        strcols = self.fmt._to_str_columns()

    def get_col_type(dtype):
        if issubclass(dtype.type, np.number):
            return 'r'
        else:
            return 'l'
    if self.fmt.index and isinstance(self.frame.index, ABCMultiIndex):
        out = self.frame.index.format(adjoin=False, sparsify=self.fmt.sparsify, names=self.fmt.has_index_names, na_rep=self.fmt.na_rep)

        def pad_empties(x):
            for pad in reversed(x):
                if pad:
                    break
            return [x[0]] + [i if i else ' ' * len(pad) for i in x[1:]]
        out = (pad_empties(i) for i in out)
        clevels = self.frame.columns.nlevels
        out = [[' ' * len(i[-1])] * clevels + i for i in out]
        cnames = self.frame.columns.names
        if any(cnames):
            new_names = [i if i else '{}' for i in cnames]
            out[self.frame.index.nlevels - 1][:clevels] = new_names
        strcols = out + strcols[1:]
    if self.column_format is None:
        dtypes = self.frame.dtypes._values
        column_format = ''.join(map(get_col_type, dtypes))
        if self.fmt.index:
            index_format = 'l' * self.frame.index.nlevels
            column_format = index_format + column_format
    elif not isinstance(self.column_format, str):
        raise AssertionError('column_format must be str or unicode, not {typ}'.format(typ=type(column_format)))
    else:
        column_format = self.column_format
    if self.longtable:
        self._write_longtable_begin(buf, column_format)
    else:
        self._write_tabular_begin(buf, column_format)
    buf.write('\\toprule\n')
    ilevels = self.frame.index.nlevels
    clevels = self.frame.columns.nlevels
    nlevels = clevels
    if self.fmt.has_index_names and self.fmt.show_index_names:
        nlevels += 1
    strrows = list(zip(*strcols))
    self.clinebuf: List[List[int]] = []
    for i, row in enumerate(strrows):
        if i == nlevels and self.fmt.header:
            buf.write('\\midrule\n')
            if self.longtable:
                buf.write('\\endhead\n')
                buf.write('\\midrule\n')
                buf.write('\\multicolumn{{{n}}}{{r}}{{{{Continued on next page}}}} \\\\\n'.format(n=len(row)))
                buf.write('\\midrule\n')
                buf.write('\\endfoot\n\n')
                buf.write('\\bottomrule\n')
                buf.write('\\endlastfoot\n')
        if self.escape:
            crow = [x.replace('\\', '\\textbackslash ').replace('_', '\\_').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#').replace('{', '\\{').replace('}', '\\}').replace('~', '\\textasciitilde ').replace('^', '\\textasciicircum ').replace('&', '\\&') if x and x != '{}' else '{}' for x in row]
        else:
            crow = [x if x else '{}' for x in row]
        if self.bold_rows and self.fmt.index:
            crow = ['\\textbf{{{x}}}'.format(x=x) if j < ilevels and x.strip() not in ['', '{}'] else x for j, x in enumerate(crow)]
        if i < clevels and self.fmt.header and self.multicolumn:
            crow = self._format_multicolumn(crow, ilevels)
        if i >= nlevels and self.fmt.index and self.multirow and (ilevels > 1):
            crow = self._format_multirow(crow, ilevels, i, strrows)
        buf.write(' & '.join(crow))
        buf.write(' \\\\\n')
        if self.multirow and i < len(strrows) - 1:
            self._print_cline(buf, i, len(strcols))
    if self.longtable:
        self._write_longtable_end(buf)
    else:
        self._write_tabular_end(buf)