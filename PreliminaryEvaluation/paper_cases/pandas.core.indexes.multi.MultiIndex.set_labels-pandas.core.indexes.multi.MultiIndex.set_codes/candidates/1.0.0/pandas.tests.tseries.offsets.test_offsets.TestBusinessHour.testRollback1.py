def testRollback1(self):
    assert self.offset1.rollback(self.d) == self.d
    assert self.offset2.rollback(self.d) == self.d
    assert self.offset3.rollback(self.d) == self.d
    assert self.offset4.rollback(self.d) == self.d
    assert self.offset5.rollback(self.d) == datetime(2014, 6, 30, 14, 30)
    assert self.offset6.rollback(self.d) == datetime(2014, 7, 1, 5, 0)
    assert self.offset7.rollback(self.d) == datetime(2014, 7, 1, 6, 30)
    assert self.offset8.rollback(self.d) == self.d
    assert self.offset9.rollback(self.d) == self.d
    assert self.offset10.rollback(self.d) == datetime(2014, 7, 1, 2)
    d = datetime(2014, 7, 1, 0)
    assert self.offset1.rollback(d) == datetime(2014, 6, 30, 17)
    assert self.offset2.rollback(d) == datetime(2014, 6, 30, 17)
    assert self.offset3.rollback(d) == datetime(2014, 6, 30, 17)
    assert self.offset4.rollback(d) == datetime(2014, 6, 30, 17)
    assert self.offset5.rollback(d) == datetime(2014, 6, 30, 14, 30)
    assert self.offset6.rollback(d) == d
    assert self.offset7.rollback(d) == d
    assert self.offset8.rollback(d) == datetime(2014, 6, 30, 17)
    assert self.offset9.rollback(d) == d
    assert self.offset10.rollback(d) == d
    assert self._offset(5).rollback(self.d) == self.d