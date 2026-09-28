@property
def _workbook_class(self):
    from openpyxl import Workbook
    return Workbook