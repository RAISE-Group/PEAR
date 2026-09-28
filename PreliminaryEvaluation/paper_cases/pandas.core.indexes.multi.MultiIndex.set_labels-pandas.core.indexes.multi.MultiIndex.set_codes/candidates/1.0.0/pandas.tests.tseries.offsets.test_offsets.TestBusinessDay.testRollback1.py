def testRollback1(self):
    assert BDay(10).rollback(self.d) == self.d