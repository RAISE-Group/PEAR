def _write_variable_labels(self):
    self._update_map('variable_labels')
    bio = BytesIO()
    vl_len = 80 if self._dta_version == 117 else 320
    blank = _pad_bytes_new('', vl_len + 1)
    if self._variable_labels is None:
        for _ in range(self.nvar):
            bio.write(blank)
        bio.seek(0)
        self._file.write(self._tag(bio.read(), 'variable_labels'))
        return
    for col in self.data:
        if col in self._variable_labels:
            label = self._variable_labels[col]
            if len(label) > 80:
                raise ValueError('Variable labels must be 80 characters or fewer')
            try:
                encoded = label.encode(self._encoding)
            except UnicodeEncodeError:
                raise ValueError(f'Variable labels must contain only characters that can be encoded in {self._encoding}')
            bio.write(_pad_bytes_new(encoded, vl_len + 1))
        else:
            bio.write(blank)
    bio.seek(0)
    self._file.write(self._tag(bio.read(), 'variable_labels'))