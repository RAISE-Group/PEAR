def _write_variable_types(self):
    self._update_map('variable_types')
    bio = BytesIO()
    for typ in self.typlist:
        bio.write(struct.pack(self._byteorder + 'H', typ))
    bio.seek(0)
    self._file.write(self._tag(bio.read(), 'variable_types'))