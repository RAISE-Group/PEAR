def test_insert_empty(self):
    idx = timedelta_range('1 Day', periods=3)
    td = idx[0]
    idx[:0].insert(0, td)
    idx[:0].insert(1, td)
    idx[:0].insert(-1, td)