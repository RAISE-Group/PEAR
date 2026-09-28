def _get_sheet_name(self, sheet_name):
    if sheet_name is None:
        sheet_name = self.cur_sheet
    if sheet_name is None:
        raise ValueError('Must pass explicit sheet_name or set cur_sheet property')
    return sheet_name