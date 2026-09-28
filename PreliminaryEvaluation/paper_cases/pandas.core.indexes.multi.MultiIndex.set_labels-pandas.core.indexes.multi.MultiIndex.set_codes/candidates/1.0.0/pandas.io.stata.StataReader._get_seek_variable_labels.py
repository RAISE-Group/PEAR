def _get_seek_variable_labels(self):
    if self.format_version == 117:
        self.path_or_buf.read(8)
        return self._seek_value_label_names + 33 * self.nvar + 20 + 17
    elif self.format_version >= 118:
        return struct.unpack(self.byteorder + 'q', self.path_or_buf.read(8))[0] + 17
    else:
        raise ValueError()