def _get_formatted_column_labels(self, frame: 'DataFrame') -> List[List[str]]:
    from pandas.core.indexes.multi import _sparsify
    columns = frame.columns
    if isinstance(columns, ABCMultiIndex):
        fmt_columns = columns.format(sparsify=False, adjoin=False)
        fmt_columns = list(zip(*fmt_columns))
        dtypes = self.frame.dtypes._values
        restrict_formatting = any((l.is_floating for l in columns.levels))
        need_leadsp = dict(zip(fmt_columns, map(is_numeric_dtype, dtypes)))

        def space_format(x, y):
            if y not in self.formatters and need_leadsp[x] and (not restrict_formatting):
                return ' ' + y
            return y
        str_columns = list(zip(*[[space_format(x, y) for y in x] for x in fmt_columns]))
        if self.sparsify and len(str_columns):
            str_columns = _sparsify(str_columns)
        str_columns = [list(x) for x in zip(*str_columns)]
    else:
        fmt_columns = columns.format()
        dtypes = self.frame.dtypes
        need_leadsp = dict(zip(fmt_columns, map(is_numeric_dtype, dtypes)))
        str_columns = [[' ' + x if not self._get_formatter(i) and need_leadsp[x] else x] for i, (col, x) in enumerate(zip(columns, fmt_columns))]
    return str_columns