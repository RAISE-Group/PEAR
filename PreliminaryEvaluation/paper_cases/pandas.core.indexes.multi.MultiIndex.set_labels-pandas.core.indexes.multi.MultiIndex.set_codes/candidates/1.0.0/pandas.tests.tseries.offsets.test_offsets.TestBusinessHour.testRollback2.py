def testRollback2(self):
    assert self._offset(-3).rollback(datetime(2014, 7, 5, 15, 0)) == datetime(2014, 7, 4, 17, 0)