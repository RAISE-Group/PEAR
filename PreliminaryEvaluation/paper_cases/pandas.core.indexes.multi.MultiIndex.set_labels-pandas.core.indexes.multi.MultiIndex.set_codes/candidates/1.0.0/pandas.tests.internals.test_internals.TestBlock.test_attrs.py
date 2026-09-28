def test_attrs(self):
    assert self.fblock.shape == self.fblock.values.shape
    assert self.fblock.dtype == self.fblock.values.dtype
    assert len(self.fblock) == len(self.fblock.values)