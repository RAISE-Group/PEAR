def testRollforward2(self):
    assert self._offset(-3).rollforward(datetime(2014, 7, 5, 16, 0)) == datetime(2014, 7, 7, 9)