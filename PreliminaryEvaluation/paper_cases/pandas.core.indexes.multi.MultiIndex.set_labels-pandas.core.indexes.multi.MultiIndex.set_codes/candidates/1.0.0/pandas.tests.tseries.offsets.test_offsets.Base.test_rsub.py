def test_rsub(self):
    if self._offset is None or not hasattr(self, 'offset2'):
        return
    assert self.d - self.offset2 == (-self.offset2).apply(self.d)