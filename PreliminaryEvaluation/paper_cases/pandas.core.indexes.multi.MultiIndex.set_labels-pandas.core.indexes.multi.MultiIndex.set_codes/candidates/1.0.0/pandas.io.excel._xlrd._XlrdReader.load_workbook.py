def load_workbook(self, filepath_or_buffer):
    from xlrd import open_workbook
    if hasattr(filepath_or_buffer, 'read'):
        data = filepath_or_buffer.read()
        return open_workbook(file_contents=data)
    else:
        return open_workbook(filepath_or_buffer)