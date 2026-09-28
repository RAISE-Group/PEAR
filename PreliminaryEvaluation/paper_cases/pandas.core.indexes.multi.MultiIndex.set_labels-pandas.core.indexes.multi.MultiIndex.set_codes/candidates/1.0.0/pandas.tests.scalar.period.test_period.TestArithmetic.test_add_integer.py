def test_add_integer(self):
    per1 = Period(freq='D', year=2008, month=1, day=1)
    per2 = Period(freq='D', year=2008, month=1, day=2)
    assert per1 + 1 == per2
    assert 1 + per1 == per2