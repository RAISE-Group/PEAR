def _print_cline(self, buf: IO[str], i: int, icol: int) -> None:
    """
        Print clines after multirow-blocks are finished.
        """
    for cl in self.clinebuf:
        if cl[0] == i:
            buf.write('\\cline{{{cl:d}-{icol:d}}}\n'.format(cl=cl[1], icol=icol))
    self.clinebuf = [x for x in self.clinebuf if x[0] != i]