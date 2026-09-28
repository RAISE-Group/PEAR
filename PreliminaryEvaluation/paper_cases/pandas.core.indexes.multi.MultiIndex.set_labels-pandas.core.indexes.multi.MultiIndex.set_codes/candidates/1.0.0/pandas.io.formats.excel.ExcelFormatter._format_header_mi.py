def _format_header_mi(self):
    if self.columns.nlevels > 1:
        if not self.index:
            raise NotImplementedError("Writing to Excel with MultiIndex columns and no index ('index'=False) is not yet implemented.")
    has_aliases = isinstance(self.header, (tuple, list, np.ndarray, Index))
    if not (has_aliases or self.header):
        return
    columns = self.columns
    level_strs = columns.format(sparsify=self.merge_cells, adjoin=False, names=False)
    level_lengths = get_level_lengths(level_strs)
    coloffset = 0
    lnum = 0
    if self.index and isinstance(self.df.index, ABCMultiIndex):
        coloffset = len(self.df.index[0]) - 1
    if self.merge_cells:
        for lnum in range(len(level_lengths)):
            name = columns.names[lnum]
            yield ExcelCell(lnum, coloffset, name, self.header_style)
        for lnum, (spans, levels, level_codes) in enumerate(zip(level_lengths, columns.levels, columns.codes)):
            values = levels.take(level_codes)
            for i in spans:
                if spans[i] > 1:
                    yield ExcelCell(lnum, coloffset + i + 1, values[i], self.header_style, lnum, coloffset + i + spans[i])
                else:
                    yield ExcelCell(lnum, coloffset + i + 1, values[i], self.header_style)
    else:
        for i, values in enumerate(zip(*level_strs)):
            v = '.'.join(map(pprint_thing, values))
            yield ExcelCell(lnum, coloffset + i + 1, v, self.header_style)
    self.rowcounter = lnum