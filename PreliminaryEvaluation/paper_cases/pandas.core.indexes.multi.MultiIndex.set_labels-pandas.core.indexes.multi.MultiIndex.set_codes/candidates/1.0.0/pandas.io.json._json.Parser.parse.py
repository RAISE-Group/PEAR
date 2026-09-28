def parse(self):
    numpy = self.numpy
    if numpy:
        self._parse_numpy()
    else:
        self._parse_no_numpy()
    if self.obj is None:
        return None
    if self.convert_axes:
        self._convert_axes()
    self._try_convert_types()
    return self.obj