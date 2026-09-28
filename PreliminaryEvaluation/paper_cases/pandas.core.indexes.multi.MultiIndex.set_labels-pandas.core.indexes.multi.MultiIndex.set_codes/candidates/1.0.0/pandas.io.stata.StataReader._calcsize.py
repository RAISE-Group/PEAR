def _calcsize(self, fmt):
    return type(fmt) is int and fmt or struct.calcsize(self.byteorder + fmt)