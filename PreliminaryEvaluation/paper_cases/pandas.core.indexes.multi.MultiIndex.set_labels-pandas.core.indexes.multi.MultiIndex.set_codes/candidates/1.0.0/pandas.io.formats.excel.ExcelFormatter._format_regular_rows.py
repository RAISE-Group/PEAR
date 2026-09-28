def _format_regular_rows(self):
    has_aliases = isinstance(self.header, (tuple, list, np.ndarray, Index))
    if has_aliases or self.header:
        self.rowcounter += 1
    if self.index:
        if self.index_label and isinstance(self.index_label, (list, tuple, np.ndarray, Index)):
            index_label = self.index_label[0]
        elif self.index_label and isinstance(self.index_label, str):
            index_label = self.index_label
        else:
            index_label = self.df.index.names[0]
        if isinstance(self.columns, ABCMultiIndex):
            self.rowcounter += 1
        if index_label and self.header is not False:
            yield ExcelCell(self.rowcounter - 1, 0, index_label, self.header_style)
        index_values = self.df.index
        if isinstance(self.df.index, ABCPeriodIndex):
            index_values = self.df.index.to_timestamp()
        for idx, idxval in enumerate(index_values):
            yield ExcelCell(self.rowcounter + idx, 0, idxval, self.header_style)
        coloffset = 1
    else:
        coloffset = 0
    for cell in self._generate_body(coloffset):
        yield cell