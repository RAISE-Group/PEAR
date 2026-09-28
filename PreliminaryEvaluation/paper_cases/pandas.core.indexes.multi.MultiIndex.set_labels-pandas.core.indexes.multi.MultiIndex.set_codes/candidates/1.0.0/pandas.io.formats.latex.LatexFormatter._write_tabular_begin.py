def _write_tabular_begin(self, buf, column_format: str):
    """
        Write the beginning of a tabular environment or
        nested table/tabular environments including caption and label.

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
    if self.caption is not None or self.label is not None:
        if self.caption is None:
            caption_ = ''
        else:
            caption_ = '\n\\caption{{{}}}'.format(self.caption)
        if self.label is None:
            label_ = ''
        else:
            label_ = '\n\\label{{{}}}'.format(self.label)
        buf.write('\\begin{{table}}\n\\centering{}{}\n'.format(caption_, label_))
    else:
        pass
    buf.write('\\begin{{tabular}}{{{fmt}}}\n'.format(fmt=column_format))