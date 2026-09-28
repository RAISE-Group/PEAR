def testRollback2(self):
    assert CDay(10).rollback(datetime(2008, 1, 5)) == datetime(2008, 1, 4)