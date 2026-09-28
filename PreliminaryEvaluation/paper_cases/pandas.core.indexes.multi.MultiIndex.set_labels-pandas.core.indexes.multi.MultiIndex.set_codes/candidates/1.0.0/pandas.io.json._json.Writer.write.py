def write(self):
    return self._write(self.obj, self.orient, self.double_precision, self.ensure_ascii, self.date_unit, self.date_format == 'iso', self.default_handler, self.indent)