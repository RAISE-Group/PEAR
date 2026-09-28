def _write_varnames(self):
    self._update_map('varnames')
    bio = BytesIO()
    vn_len = 32 if self._dta_version == 117 else 128
    for name in self.varlist:
        name = self._null_terminate(name, True)
        name = _pad_bytes_new(name[:32].encode(self._encoding), vn_len + 1)
        bio.write(name)
    bio.seek(0)
    self._file.write(self._tag(bio.read(), 'varnames'))