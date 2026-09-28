def _write_value_labels(self):
    for vl in self._value_labels:
        self._file.write(vl.generate_value_label(self._byteorder))