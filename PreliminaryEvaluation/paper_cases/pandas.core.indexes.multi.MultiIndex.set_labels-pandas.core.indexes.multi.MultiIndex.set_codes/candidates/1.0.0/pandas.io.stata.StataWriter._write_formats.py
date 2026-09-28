def _write_formats(self):
    for fmt in self.fmtlist:
        self._write(_pad_bytes(fmt, 49))