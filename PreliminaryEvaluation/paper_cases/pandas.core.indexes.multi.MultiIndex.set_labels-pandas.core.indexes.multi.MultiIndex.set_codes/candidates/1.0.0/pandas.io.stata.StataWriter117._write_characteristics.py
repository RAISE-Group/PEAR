def _write_characteristics(self):
    self._update_map('characteristics')
    self._file.write(self._tag(b'', 'characteristics'))