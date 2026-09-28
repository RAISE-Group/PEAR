def setup_method(self, method):
    self.d = datetime(2008, 1, 1)
    self.nd = np_datetime64_compat('2008-01-01 00:00:00Z')
    self.offset = CDay()
    self.offset1 = self.offset
    self.offset2 = CDay(2)