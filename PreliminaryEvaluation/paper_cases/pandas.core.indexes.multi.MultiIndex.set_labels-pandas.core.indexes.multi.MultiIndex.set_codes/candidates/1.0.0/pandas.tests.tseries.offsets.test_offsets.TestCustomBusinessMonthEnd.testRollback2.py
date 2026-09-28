def testRollback2(self):
    assert CBMonthEnd(10).rollback(self.d) == datetime(2007, 12, 31)