def _read_float(self, offset, width):
    if width not in (4, 8):
        self.close()
        raise ValueError('invalid float width')
    buf = self._read_bytes(offset, width)
    fd = 'f' if width == 4 else 'd'
    return struct.unpack(self.byte_order + fd, buf)[0]