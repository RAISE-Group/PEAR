def _get_variable_labels(self):
    if self.format_version >= 118:
        vlblist = [self._decode(self.path_or_buf.read(321)) for i in range(self.nvar)]
    elif self.format_version > 105:
        vlblist = [self._decode(self.path_or_buf.read(81)) for i in range(self.nvar)]
    else:
        vlblist = [self._decode(self.path_or_buf.read(32)) for i in range(self.nvar)]
    return vlblist