def _read_int(self, offset, width):
    if width not in (1, 2, 4, 8):
        self.close()
        raise ValueError('invalid int width')
    buf = self._read_bytes(offset, width)
    it = {1: 'b', 2: 'h', 4: 'l', 8: 'q'}[width]
    iv = struct.unpack(self.byte_order + it, buf)[0]
    return iv