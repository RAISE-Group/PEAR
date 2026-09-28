def _format_multirow(self, row: List[str], ilevels: int, i: int, rows: List[Tuple[str, ...]]) -> List[str]:
    """
        Check following rows, whether row should be a multirow

        e.g.:     becomes:
        a & 0 &   \\multirow{2}{*}{a} & 0 &
          & 1 &     & 1 &
        b & 0 &   \\cline{1-2}
                  b & 0 &
        """
    for j in range(ilevels):
        if row[j].strip():
            nrow = 1
            for r in rows[i + 1:]:
                if not r[j].strip():
                    nrow += 1
                else:
                    break
            if nrow > 1:
                row[j] = '\\multirow{{{nrow:d}}}{{*}}{{{row:s}}}'.format(nrow=nrow, row=row[j].strip())
                self.clinebuf.append([i + nrow - 1, j + 1])
    return row