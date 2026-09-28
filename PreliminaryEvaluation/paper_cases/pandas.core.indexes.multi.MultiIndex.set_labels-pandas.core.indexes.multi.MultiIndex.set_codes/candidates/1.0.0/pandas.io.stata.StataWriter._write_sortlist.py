def _write_sortlist(self):
    srtlist = _pad_bytes('', 2 * (self.nvar + 1))
    self._write(srtlist)