def _write_tabular_end(self, buf):
    """
        Write the end of a tabular environment or nested table/tabular
        environment.

        Parameters
        ----------
        buf : string or file handle
            File path or object. If not specified, the result is returned as
            a string.

        """
    buf.write('\\bottomrule\n')
    buf.write('\\end{tabular}\n')
    if self.caption is not None or self.label is not None:
        buf.write('\\end{table}\n')
    else:
        pass