def _generate_body(self, coloffset: int):
    if self.styler is None:
        styles = None
    else:
        styles = self.styler._compute().ctx
        if not styles:
            styles = None
    xlstyle = None
    for colidx in range(len(self.columns)):
        series = self.df.iloc[:, colidx]
        for i, val in enumerate(series):
            if styles is not None:
                xlstyle = self.style_converter(';'.join(styles[i, colidx]))
            yield ExcelCell(self.rowcounter + i, colidx + coloffset, val, xlstyle)