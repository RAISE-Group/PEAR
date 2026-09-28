def setup_method(self, method):
    self.dtc = converter.DatetimeConverter()
    self.tc = converter.TimeFormatter(None)