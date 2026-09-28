def testRollback1(self):
    assert CDay(10).rollback(self.d) == self.d