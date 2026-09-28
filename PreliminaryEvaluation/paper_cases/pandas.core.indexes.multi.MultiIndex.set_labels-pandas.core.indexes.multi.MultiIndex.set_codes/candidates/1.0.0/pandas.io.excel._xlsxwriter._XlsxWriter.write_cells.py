def write_cells(self, cells, sheet_name=None, startrow=0, startcol=0, freeze_panes=None):
    sheet_name = self._get_sheet_name(sheet_name)
    if sheet_name in self.sheets:
        wks = self.sheets[sheet_name]
    else:
        wks = self.book.add_worksheet(sheet_name)
        self.sheets[sheet_name] = wks
    style_dict = {'null': None}
    if _validate_freeze_panes(freeze_panes):
        wks.freeze_panes(*freeze_panes)
    for cell in cells:
        val, fmt = self._value_with_fmt(cell.val)
        stylekey = json.dumps(cell.style)
        if fmt:
            stylekey += fmt
        if stylekey in style_dict:
            style = style_dict[stylekey]
        else:
            style = self.book.add_format(_XlsxStyler.convert(cell.style, fmt))
            style_dict[stylekey] = style
        if cell.mergestart is not None and cell.mergeend is not None:
            wks.merge_range(startrow + cell.row, startcol + cell.col, startrow + cell.mergestart, startcol + cell.mergeend, val, style)
        else:
            wks.write(startrow + cell.row, startcol + cell.col, val, style)