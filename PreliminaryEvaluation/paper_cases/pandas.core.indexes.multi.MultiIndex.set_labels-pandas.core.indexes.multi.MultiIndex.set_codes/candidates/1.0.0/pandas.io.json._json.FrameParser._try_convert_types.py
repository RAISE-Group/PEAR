def _try_convert_types(self):
    if self.obj is None:
        return
    if self.convert_dates:
        self._try_convert_dates()
    self._process_converter(lambda col, c: self._try_convert_data(col, c, convert_dates=False))