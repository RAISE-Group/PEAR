def load_workbook(self, filepath_or_buffer: FilePathOrBuffer):
    from odf.opendocument import load
    return load(filepath_or_buffer)