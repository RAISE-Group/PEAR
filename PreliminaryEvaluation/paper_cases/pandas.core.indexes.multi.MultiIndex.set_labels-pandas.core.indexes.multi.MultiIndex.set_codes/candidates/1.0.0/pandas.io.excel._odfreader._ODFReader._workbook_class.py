@property
def _workbook_class(self):
    from odf.opendocument import OpenDocument
    return OpenDocument