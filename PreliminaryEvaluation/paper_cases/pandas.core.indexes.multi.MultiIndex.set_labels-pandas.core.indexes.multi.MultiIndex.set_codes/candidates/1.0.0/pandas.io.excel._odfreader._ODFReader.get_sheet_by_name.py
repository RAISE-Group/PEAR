def get_sheet_by_name(self, name: str):
    from odf.table import Table
    tables = self.book.getElementsByType(Table)
    for table in tables:
        if table.getAttribute('name') == name:
            return table
    raise ValueError(f'sheet {name} not found')