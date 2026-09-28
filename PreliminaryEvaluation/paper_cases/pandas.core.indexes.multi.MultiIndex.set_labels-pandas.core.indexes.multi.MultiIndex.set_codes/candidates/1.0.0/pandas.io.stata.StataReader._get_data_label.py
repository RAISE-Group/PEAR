def _get_data_label(self):
    if self.format_version >= 118:
        strlen = struct.unpack(self.byteorder + 'H', self.path_or_buf.read(2))[0]
        return self._decode(self.path_or_buf.read(strlen))
    elif self.format_version == 117:
        strlen = struct.unpack('b', self.path_or_buf.read(1))[0]
        return self._decode(self.path_or_buf.read(strlen))
    elif self.format_version > 105:
        return self._decode(self.path_or_buf.read(81))
    else:
        return self._decode(self.path_or_buf.read(32))