def testRollforward1(self):
    assert CBMonthEnd(10).rollforward(self.d) == datetime(2008, 1, 31)