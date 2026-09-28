def test_call(self):
    assert self.offset2(self.d) == datetime(2008, 1, 3)
    assert self.offset2(self.nd) == datetime(2008, 1, 3)