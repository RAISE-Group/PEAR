def testMult1(self):
    if self._offset is None or not hasattr(self, 'offset1'):
        return
    assert self.d + 10 * self.offset1 == self.d + self._offset(10)
    assert self.d + 5 * self.offset1 == self.d + self._offset(5)