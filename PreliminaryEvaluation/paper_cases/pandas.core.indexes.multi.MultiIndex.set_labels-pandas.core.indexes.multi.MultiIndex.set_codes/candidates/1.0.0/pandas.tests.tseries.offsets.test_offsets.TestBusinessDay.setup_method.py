def setup_method(self, method):
    self.d = datetime(2008, 1, 1)
    self.offset = BDay()
    self.offset1 = self.offset
    self.offset2 = BDay(2)