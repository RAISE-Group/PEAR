def _get_varlist(self):
    if self.format_version == 117:
        b = 33
    elif self.format_version >= 118:
        b = 129
    return [self._decode(self.path_or_buf.read(b)) for i in range(self.nvar)]