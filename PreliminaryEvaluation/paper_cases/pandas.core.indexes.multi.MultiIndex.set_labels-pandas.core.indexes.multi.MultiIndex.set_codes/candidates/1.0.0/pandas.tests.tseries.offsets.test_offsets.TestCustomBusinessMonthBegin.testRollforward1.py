def testRollforward1(self):
    assert CBMonthBegin(10).rollforward(self.d) == datetime(2008, 1, 1)