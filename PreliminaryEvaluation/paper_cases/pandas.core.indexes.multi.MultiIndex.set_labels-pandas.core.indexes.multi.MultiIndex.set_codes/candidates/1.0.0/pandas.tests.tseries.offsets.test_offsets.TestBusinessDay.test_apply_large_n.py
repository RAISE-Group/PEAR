def test_apply_large_n(self):
    dt = datetime(2012, 10, 23)
    result = dt + BDay(10)
    assert result == datetime(2012, 11, 6)
    result = dt + BDay(100) - BDay(100)
    assert result == dt
    off = BDay() * 6
    rs = datetime(2012, 1, 1) - off
    xp = datetime(2011, 12, 23)
    assert rs == xp
    st = datetime(2011, 12, 18)
    rs = st + off
    xp = datetime(2011, 12, 26)
    assert rs == xp
    off = BDay() * 10
    rs = datetime(2014, 1, 5) + off
    xp = datetime(2014, 1, 17)
    assert rs == xp