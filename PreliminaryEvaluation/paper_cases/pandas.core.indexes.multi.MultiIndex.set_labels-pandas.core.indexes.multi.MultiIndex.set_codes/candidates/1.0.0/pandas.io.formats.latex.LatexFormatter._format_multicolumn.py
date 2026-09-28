def _format_multicolumn(self, row: List[str], ilevels: int) -> List[str]:
    """
        Combine columns belonging to a group to a single multicolumn entry
        according to self.multicolumn_format

        e.g.:
        a &  &  & b & c &
        will become
        \\multicolumn{3}{l}{a} & b & \\multicolumn{2}{l}{c}
        """
    row2 = list(row[:ilevels])
    ncol = 1
    coltext = ''

    def append_col():
        if ncol > 1:
            row2.append('\\multicolumn{{{ncol:d}}}{{{fmt:s}}}{{{txt:s}}}'.format(ncol=ncol, fmt=self.multicolumn_format, txt=coltext.strip()))
        else:
            row2.append(coltext)
    for c in row[ilevels:]:
        if c.strip():
            if coltext:
                append_col()
            coltext = c
            ncol = 1
        else:
            ncol += 1
    if coltext:
        append_col()
    return row2