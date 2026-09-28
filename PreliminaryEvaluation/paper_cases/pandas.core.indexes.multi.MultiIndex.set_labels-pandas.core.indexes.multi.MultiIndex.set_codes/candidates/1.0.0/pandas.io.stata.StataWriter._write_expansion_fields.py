def _write_expansion_fields(self):
    """Write 5 zeros for expansion fields"""
    self._write(_pad_bytes('', 5))