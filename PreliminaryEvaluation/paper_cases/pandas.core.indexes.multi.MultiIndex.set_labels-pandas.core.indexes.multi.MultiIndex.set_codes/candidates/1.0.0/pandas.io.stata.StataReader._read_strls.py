def _read_strls(self):
    self.path_or_buf.seek(self.seek_strls)
    self.GSO = {'0': ''}
    while True:
        if self.path_or_buf.read(3) != b'GSO':
            break
        if self.format_version == 117:
            v_o = struct.unpack(self.byteorder + 'Q', self.path_or_buf.read(8))[0]
        else:
            buf = self.path_or_buf.read(12)
            v_size = 2 if self.format_version == 118 else 3
            if self.byteorder == '<':
                buf = buf[0:v_size] + buf[4:12 - v_size]
            else:
                buf = buf[0:v_size] + buf[4 + v_size:]
            v_o = struct.unpack('Q', buf)[0]
        typ = struct.unpack('B', self.path_or_buf.read(1))[0]
        length = struct.unpack(self.byteorder + 'I', self.path_or_buf.read(4))[0]
        va = self.path_or_buf.read(length)
        if typ == 130:
            va = va[0:-1].decode(self._encoding)
        self.GSO[str(v_o)] = va