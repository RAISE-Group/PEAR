@property
def _workbook_class(self):
    from xlrd import Book
    return Book