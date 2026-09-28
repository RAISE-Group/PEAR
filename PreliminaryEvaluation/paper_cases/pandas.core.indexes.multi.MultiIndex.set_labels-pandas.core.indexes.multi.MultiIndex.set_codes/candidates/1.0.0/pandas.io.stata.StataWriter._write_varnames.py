def _write_varnames(self):
    for name in self.varlist:
        name = self._null_terminate(name, True)
        name = _pad_bytes(name[:32], 33)
        self._write(name)