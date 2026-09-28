def setup_method(self, method):
    self.d = datetime(2008, 1, 1)
    self.offset = self._offset()
    self.offset1 = self.offset
    self.offset2 = self._offset(2)