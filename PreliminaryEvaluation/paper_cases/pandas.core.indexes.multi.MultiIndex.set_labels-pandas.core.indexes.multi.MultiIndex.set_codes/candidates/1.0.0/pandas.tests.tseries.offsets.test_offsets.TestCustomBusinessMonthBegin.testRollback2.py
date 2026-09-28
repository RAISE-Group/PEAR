def testRollback2(self):
    assert CBMonthBegin(10).rollback(self.d) == datetime(2008, 1, 1)