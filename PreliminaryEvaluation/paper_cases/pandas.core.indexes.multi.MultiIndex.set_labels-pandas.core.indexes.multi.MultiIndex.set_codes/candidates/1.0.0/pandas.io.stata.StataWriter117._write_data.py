def _write_data(self):
    self._update_map('data')
    data = self.data
    self._file.write(b'<data>')
    self._file.write(data.tobytes())
    self._file.write(b'</data>')