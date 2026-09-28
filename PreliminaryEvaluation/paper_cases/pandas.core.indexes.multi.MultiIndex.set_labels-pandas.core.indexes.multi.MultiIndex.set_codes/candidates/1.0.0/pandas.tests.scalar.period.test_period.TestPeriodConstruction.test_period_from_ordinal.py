def test_period_from_ordinal(self):
    p = Period('2011-01', freq='M')
    res = Period._from_ordinal(p.ordinal, freq='M')
    assert p == res
    assert isinstance(res, Period)