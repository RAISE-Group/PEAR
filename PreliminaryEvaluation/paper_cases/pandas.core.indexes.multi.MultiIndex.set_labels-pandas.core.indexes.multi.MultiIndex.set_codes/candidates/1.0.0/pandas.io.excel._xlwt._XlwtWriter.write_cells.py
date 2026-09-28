def write_cells(self, cells, sheet_name=None, startrow=0, startcol=0, freeze_panes=None):
    sheet_name = self._get_sheet_name(sheet_name)
    if sheet_name in self.sheets:
        wks = self.sheets[sheet_name]
    else:
        wks = self.book.add_sheet(sheet_name)
        self.sheets[sheet_name] = wks
    if _validate_freeze_panes(freeze_panes):
        wks.set_panes_frozen(True)
        wks.set_horz_split_pos(freeze_panes[0])
        wks.set_vert_split_pos(freeze_panes[1])
    style_dict = {}
    for cell in cells:
        val, fmt = self._value_with_fmt(cell.val)
        stylekey = json.dumps(cell.style)
        if fmt:
            stylekey += fmt
        if stylekey in style_dict:
            style = style_dict[stylekey]
        else:
            style = self._convert_to_style(cell.style, fmt)
            style_dict[stylekey] = style
        if cell.mergestart is not None and cell.mergeend is not None:
            wks.write_merge(startrow + cell.row, startrow + cell.mergestart, startcol + cell.col, startcol + cell.mergeend, val, style)
        else:
            wks.write(startrow + cell.row, startcol + cell.col, val, style)