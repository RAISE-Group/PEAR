def _write_variable_types(self):
    for typ in self.typlist:
        self._file.write(struct.pack('B', typ))