def testRollforward2(self):
    assert BDay(10).rollforward(datetime(2008, 1, 5)) == datetime(2008, 1, 7)