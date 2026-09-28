def _get_fmtlist(self):
    if self.format_version >= 118:
        b = 57
    elif self.format_version > 113:
        b = 49
    elif self.format_version > 104:
        b = 12
    else:
        b = 7
    return [self._decode(self.path_or_buf.read(b)) for i in range(self.nvar)]