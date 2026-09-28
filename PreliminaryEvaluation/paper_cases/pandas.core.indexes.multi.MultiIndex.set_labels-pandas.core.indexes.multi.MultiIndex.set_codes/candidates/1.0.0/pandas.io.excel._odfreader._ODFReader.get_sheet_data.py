def get_sheet_data(self, sheet, convert_float: bool) -> List[List[Scalar]]:
    """Parse an ODF Table into a list of lists
        """
    from odf.table import CoveredTableCell, TableCell, TableRow
    covered_cell_name = CoveredTableCell().qname
    table_cell_name = TableCell().qname
    cell_names = {covered_cell_name, table_cell_name}
    sheet_rows = sheet.getElementsByType(TableRow)
    empty_rows = 0
    max_row_len = 0
    table: List[List[Scalar]] = []
    for i, sheet_row in enumerate(sheet_rows):
        sheet_cells = [x for x in sheet_row.childNodes if x.qname in cell_names]
        empty_cells = 0
        table_row: List[Scalar] = []
        for j, sheet_cell in enumerate(sheet_cells):
            if sheet_cell.qname == table_cell_name:
                value = self._get_cell_value(sheet_cell, convert_float)
            else:
                value = self.empty_value
            column_repeat = self._get_column_repeat(sheet_cell)
            if value == self.empty_value:
                empty_cells += column_repeat
            else:
                table_row.extend([self.empty_value] * empty_cells)
                empty_cells = 0
                table_row.extend([value] * column_repeat)
        if max_row_len < len(table_row):
            max_row_len = len(table_row)
        row_repeat = self._get_row_repeat(sheet_row)
        if self._is_empty_row(sheet_row):
            empty_rows += row_repeat
        else:
            table.extend([[self.empty_value]] * empty_rows)
            empty_rows = 0
            for _ in range(row_repeat):
                table.append(table_row)
    for row in table:
        if len(row) < max_row_len:
            row.extend([self.empty_value] * (max_row_len - len(row)))
    return table