def load_workbook(self, filepath_or_buffer: FilePathOrBuffer):
    from pyxlsb import open_workbook
    return open_workbook(filepath_or_buffer)