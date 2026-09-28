def testMult2(self):
    if self._offset is None:
        return
    assert self.d + -5 * self._offset(-10) == self.d + self._offset(50)
    assert self.d + -3 * self._offset(-2) == self.d + self._offset(6)