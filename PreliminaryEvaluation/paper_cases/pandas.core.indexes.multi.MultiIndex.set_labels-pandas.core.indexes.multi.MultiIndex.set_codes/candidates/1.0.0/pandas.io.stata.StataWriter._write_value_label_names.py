def _write_value_label_names(self):
    for i in range(self.nvar):
        if self._is_col_cat[i]:
            name = self.varlist[i]
            name = self._null_terminate(name, True)
            name = _pad_bytes(name[:32], 33)
            self._write(name)
        else:
            self._write(_pad_bytes('', 33))