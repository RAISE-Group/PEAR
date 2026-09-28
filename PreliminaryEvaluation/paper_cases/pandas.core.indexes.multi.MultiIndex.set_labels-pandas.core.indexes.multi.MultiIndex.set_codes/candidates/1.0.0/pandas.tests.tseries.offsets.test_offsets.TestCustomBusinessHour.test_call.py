def test_call(self):
    assert self.offset1(self.d) == datetime(2014, 7, 1, 11)
    assert self.offset2(self.d) == datetime(2014, 7, 1, 11)