def _write_longtable_begin(self, buf, column_format: str):
    """
        Write the beginning of a longtable environment including caption and
        label if provided by user.

        Parameters
        ----------
        buf : string or file handle
            File path or object. If not specified, the result is returned as
            a string.
        column_format : str
            The columns format as specified in `LaTeX table format
            <https://en.wikibooks.org/wiki/LaTeX/Tables>`__ e.g 'rcl'
            for 3 columns
        """
    buf.write('\\begin{{longtable}}{{{fmt}}}\n'.format(fmt=column_format))
    if self.caption is not None or self.label is not None:
        if self.caption is None:
            pass
        else:
            buf.write('\\caption{{{}}}'.format(self.caption))
        if self.label is None:
            pass
        else:
            buf.write('\\label{{{}}}'.format(self.label))
        buf.write('\\\\\n')
    else:
        pass