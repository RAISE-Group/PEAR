def _get_nobs(self):
    if self.format_version >= 118:
        return struct.unpack(self.byteorder + 'Q', self.path_or_buf.read(8))[0]
    else:
        return struct.unpack(self.byteorder + 'I', self.path_or_buf.read(4))[0]