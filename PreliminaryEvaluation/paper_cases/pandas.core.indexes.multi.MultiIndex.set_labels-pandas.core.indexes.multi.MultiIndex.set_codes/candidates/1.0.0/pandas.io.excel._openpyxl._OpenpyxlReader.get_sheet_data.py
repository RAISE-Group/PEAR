def get_sheet_data(self, sheet, convert_float: bool) -> List[List[Scalar]]:
    data: List[List[Scalar]] = []
    for row in sheet.rows:
        data.append([self._convert_cell(cell, convert_float) for cell in row])
    return data