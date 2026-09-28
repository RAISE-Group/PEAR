def _try_convert_types(self):
    if self.obj is None:
        return
    obj, result = self._try_convert_data('data', self.obj, convert_dates=self.convert_dates)
    if result:
        self.obj = obj