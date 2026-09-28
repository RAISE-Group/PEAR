def _format_hierarchical_rows(self):
    has_aliases = isinstance(self.header, (tuple, list, np.ndarray, Index))
    if has_aliases or self.header:
        self.rowcounter += 1
    gcolidx = 0
    if self.index:
        index_labels = self.df.index.names
        if self.index_label and isinstance(self.index_label, (list, tuple, np.ndarray, Index)):
            index_labels = self.index_label
        if isinstance(self.columns, ABCMultiIndex) and self.merge_cells:
            self.rowcounter += 1
        if com.any_not_none(*index_labels) and self.header is not False:
            for cidx, name in enumerate(index_labels):
                yield ExcelCell(self.rowcounter - 1, cidx, name, self.header_style)
        if self.merge_cells:
            level_strs = self.df.index.format(sparsify=True, adjoin=False, names=False)
            level_lengths = get_level_lengths(level_strs)
            for spans, levels, level_codes in zip(level_lengths, self.df.index.levels, self.df.index.codes):
                values = levels.take(level_codes, allow_fill=levels._can_hold_na, fill_value=True)
                for i in spans:
                    if spans[i] > 1:
                        yield ExcelCell(self.rowcounter + i, gcolidx, values[i], self.header_style, self.rowcounter + i + spans[i] - 1, gcolidx)
                    else:
                        yield ExcelCell(self.rowcounter + i, gcolidx, values[i], self.header_style)
                gcolidx += 1
        else:
            for indexcolvals in zip(*self.df.index):
                for idx, indexcolval in enumerate(indexcolvals):
                    yield ExcelCell(self.rowcounter + idx, gcolidx, indexcolval, self.header_style)
                gcolidx += 1
    for cell in self._generate_body(gcolidx):
        yield cell