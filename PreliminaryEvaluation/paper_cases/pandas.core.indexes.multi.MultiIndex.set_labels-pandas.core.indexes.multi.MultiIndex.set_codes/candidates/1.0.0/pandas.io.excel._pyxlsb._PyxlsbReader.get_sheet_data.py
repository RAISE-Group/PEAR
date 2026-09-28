def get_sheet_data(self, sheet, convert_float: bool) -> List[List[Scalar]]:
    return [[self._convert_cell(c, convert_float) for c in r] for r in sheet.rows(sparse=False)]