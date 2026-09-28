@property
def sheet_names(self) -> List[str]:
    """Return a list of sheet names present in the document"""
    from odf.table import Table
    tables = self.book.getElementsByType(Table)
    return [t.getAttribute('name') for t in tables]