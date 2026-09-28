def testRollback1(self):
    assert self.offset1.rollback(self.d) == self.d
    assert self.offset2.rollback(self.d) == self.d
    d = datetime(2014, 7, 1, 0)
    assert self.offset1.rollback(d) == datetime(2014, 6, 27, 17)
    assert self.offset2.rollback(d) == datetime(2014, 6, 26, 17)