def _write_sortlist(self):
    self._update_map('sortlist')
    sort_size = 2 if self._dta_version < 119 else 4
    self._file.write(self._tag(b'\x00' * sort_size * (self.nvar + 1), 'sortlist'))