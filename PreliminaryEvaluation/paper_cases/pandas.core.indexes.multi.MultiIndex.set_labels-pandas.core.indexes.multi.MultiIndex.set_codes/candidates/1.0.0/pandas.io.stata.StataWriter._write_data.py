def _write_data(self):
    data = self.data
    self._file.write(data.tobytes())