def get_sheet_by_index(self, index: int):
    from odf.table import Table
    tables = self.book.getElementsByType(Table)
    return tables[index]