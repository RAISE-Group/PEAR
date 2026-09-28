def to_string(self) -> str:
    series = self.tr_series
    footer = self._get_footer()
    if len(series) == 0:
        return '{name}([], {footer})'.format(name=type(self.series).__name__, footer=footer)
    fmt_index, have_header = self._get_formatted_index()
    fmt_values = self._get_formatted_values()
    if self.truncate_v:
        n_header_rows = 0
        row_num = self.tr_row_num
        row_num = cast(int, row_num)
        width = self.adj.len(fmt_values[row_num - 1])
        if width > 3:
            dot_str = '...'
        else:
            dot_str = '..'
        dot_str = self.adj.justify([dot_str], width, mode='center')[0]
        fmt_values.insert(row_num + n_header_rows, dot_str)
        fmt_index.insert(row_num + 1, '')
    if self.index:
        result = self.adj.adjoin(3, *[fmt_index[1:], fmt_values])
    else:
        result = self.adj.adjoin(3, fmt_values)
    if self.header and have_header:
        result = fmt_index[0] + '\n' + result
    if footer:
        result += '\n' + footer
    return str(''.join(result))