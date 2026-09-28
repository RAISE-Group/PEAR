def testRollback1(self):
    assert CDay(10).rollback(datetime(2007, 12, 31)) == datetime(2007, 12, 31)