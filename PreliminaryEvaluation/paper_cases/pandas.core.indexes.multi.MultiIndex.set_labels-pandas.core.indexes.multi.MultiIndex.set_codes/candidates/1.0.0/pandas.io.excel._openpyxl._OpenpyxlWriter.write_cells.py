def write_cells(self, cells, sheet_name=None, startrow=0, startcol=0, freeze_panes=None):
    sheet_name = self._get_sheet_name(sheet_name)
    _style_cache = {}
    if sheet_name in self.sheets:
        wks = self.sheets[sheet_name]
    else:
        wks = self.book.create_sheet()
        wks.title = sheet_name
        self.sheets[sheet_name] = wks
    if _validate_freeze_panes(freeze_panes):
        wks.freeze_panes = wks.cell(row=freeze_panes[0] + 1, column=freeze_panes[1] + 1)
    for cell in cells:
        xcell = wks.cell(row=startrow + cell.row + 1, column=startcol + cell.col + 1)
        xcell.value, fmt = self._value_with_fmt(cell.val)
        if fmt:
            xcell.number_format = fmt
        style_kwargs = {}
        if cell.style:
            key = str(cell.style)
            style_kwargs = _style_cache.get(key)
            if style_kwargs is None:
                style_kwargs = self._convert_to_style_kwargs(cell.style)
                _style_cache[key] = style_kwargs
        if style_kwargs:
            for k, v in style_kwargs.items():
                setattr(xcell, k, v)
        if cell.mergestart is not None and cell.mergeend is not None:
            wks.merge_cells(start_row=startrow + cell.row + 1, start_column=startcol + cell.col + 1, end_column=startcol + cell.mergeend + 1, end_row=startrow + cell.mergestart + 1)
            if style_kwargs:
                first_row = startrow + cell.row + 1
                last_row = startrow + cell.mergestart + 1
                first_col = startcol + cell.col + 1
                last_col = startcol + cell.mergeend + 1
                for row in range(first_row, last_row + 1):
                    for col in range(first_col, last_col + 1):
                        if row == first_row and col == first_col:
                            continue
                        xcell = wks.cell(column=col, row=row)
                        for k, v in style_kwargs.items():
                            setattr(xcell, k, v)