def _write_value_label_names(self):
    self._update_map('value_label_names')
    bio = BytesIO()
    vl_len = 32 if self._dta_version == 117 else 128
    for i in range(self.nvar):
        name = ''
        if self._is_col_cat[i]:
            name = self.varlist[i]
        name = self._null_terminate(name, True)
        name = _pad_bytes_new(name[:32].encode(self._encoding), vl_len + 1)
        bio.write(name)
    bio.seek(0)
    self._file.write(self._tag(bio.read(), 'value_label_names'))