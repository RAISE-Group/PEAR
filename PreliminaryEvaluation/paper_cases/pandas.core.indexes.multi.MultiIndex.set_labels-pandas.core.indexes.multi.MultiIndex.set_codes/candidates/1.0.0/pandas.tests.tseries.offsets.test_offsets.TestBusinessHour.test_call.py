def test_call(self):
    assert self.offset1(self.d) == datetime(2014, 7, 1, 11)
    assert self.offset2(self.d) == datetime(2014, 7, 1, 13)
    assert self.offset3(self.d) == datetime(2014, 6, 30, 17)
    assert self.offset4(self.d) == datetime(2014, 6, 30, 14)
    assert self.offset8(self.d) == datetime(2014, 7, 1, 11)
    assert self.offset9(self.d) == datetime(2014, 7, 1, 22)
    assert self.offset10(self.d) == datetime(2014, 7, 1, 1)