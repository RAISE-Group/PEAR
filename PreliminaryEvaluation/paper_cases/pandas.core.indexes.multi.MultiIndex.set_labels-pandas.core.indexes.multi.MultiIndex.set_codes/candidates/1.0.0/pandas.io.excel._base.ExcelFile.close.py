def close(self):
    """close io if necessary"""
    if self.engine == 'openpyxl':
        wb = self.book
        wb._archive.close()
    if hasattr(self.io, 'close'):
        self.io.close()