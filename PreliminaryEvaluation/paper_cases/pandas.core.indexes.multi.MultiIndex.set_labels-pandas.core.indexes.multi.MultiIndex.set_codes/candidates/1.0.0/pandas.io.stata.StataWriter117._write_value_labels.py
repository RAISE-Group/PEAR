def _write_value_labels(self):
    self._update_map('value_labels')
    bio = BytesIO()
    for vl in self._value_labels:
        lab = vl.generate_value_label(self._byteorder)
        lab = self._tag(lab, 'lbl')
        bio.write(lab)
    bio.seek(0)
    self._file.write(self._tag(bio.read(), 'value_labels'))