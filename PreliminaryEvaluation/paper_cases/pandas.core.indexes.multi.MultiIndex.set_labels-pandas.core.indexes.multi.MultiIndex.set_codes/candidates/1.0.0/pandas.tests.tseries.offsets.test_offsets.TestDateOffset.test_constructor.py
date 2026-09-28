def test_constructor(self):
    assert self.d + DateOffset(months=2) == datetime(2008, 3, 2)
    assert self.d - DateOffset(months=2) == datetime(2007, 11, 2)
    assert self.d + DateOffset(2) == datetime(2008, 1, 4)
    assert not DateOffset(2).is_anchored()
    assert DateOffset(1).is_anchored()
    d = datetime(2008, 1, 31)
    assert d + DateOffset(months=1) == datetime(2008, 2, 29)