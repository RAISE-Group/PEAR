def testRollforward1(self):
    assert self.offset1.rollforward(self.d) == self.d
    assert self.offset2.rollforward(self.d) == self.d
    d = datetime(2014, 7, 1, 0)
    assert self.offset1.rollforward(d) == datetime(2014, 7, 1, 9)
    assert self.offset2.rollforward(d) == datetime(2014, 7, 1, 9)