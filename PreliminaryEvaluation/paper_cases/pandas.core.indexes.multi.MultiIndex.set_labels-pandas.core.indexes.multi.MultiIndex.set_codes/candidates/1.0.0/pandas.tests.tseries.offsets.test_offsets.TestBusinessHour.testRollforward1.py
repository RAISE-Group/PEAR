def testRollforward1(self):
    assert self.offset1.rollforward(self.d) == self.d
    assert self.offset2.rollforward(self.d) == self.d
    assert self.offset3.rollforward(self.d) == self.d
    assert self.offset4.rollforward(self.d) == self.d
    assert self.offset5.rollforward(self.d) == datetime(2014, 7, 1, 11, 0)
    assert self.offset6.rollforward(self.d) == datetime(2014, 7, 1, 20, 0)
    assert self.offset7.rollforward(self.d) == datetime(2014, 7, 1, 21, 30)
    assert self.offset8.rollforward(self.d) == self.d
    assert self.offset9.rollforward(self.d) == self.d
    assert self.offset10.rollforward(self.d) == datetime(2014, 7, 1, 13)
    d = datetime(2014, 7, 1, 0)
    assert self.offset1.rollforward(d) == datetime(2014, 7, 1, 9)
    assert self.offset2.rollforward(d) == datetime(2014, 7, 1, 9)
    assert self.offset3.rollforward(d) == datetime(2014, 7, 1, 9)
    assert self.offset4.rollforward(d) == datetime(2014, 7, 1, 9)
    assert self.offset5.rollforward(d) == datetime(2014, 7, 1, 11)
    assert self.offset6.rollforward(d) == d
    assert self.offset7.rollforward(d) == d
    assert self.offset8.rollforward(d) == datetime(2014, 7, 1, 9)
    assert self.offset9.rollforward(d) == d
    assert self.offset10.rollforward(d) == d
    assert self._offset(5).rollforward(self.d) == self.d