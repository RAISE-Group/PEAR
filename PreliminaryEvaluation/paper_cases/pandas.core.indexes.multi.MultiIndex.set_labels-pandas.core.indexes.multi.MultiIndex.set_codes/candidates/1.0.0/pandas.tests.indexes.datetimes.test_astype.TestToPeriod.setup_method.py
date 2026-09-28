def setup_method(self, method):
    data = [Timestamp('2007-01-01 10:11:12.123456Z'), Timestamp('2007-01-01 10:11:13.789123Z')]
    self.index = DatetimeIndex(data)