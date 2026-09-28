def test_daterange_bug_456(self):
    rng1 = bdate_range('12/5/2011', '12/5/2011')
    rng2 = bdate_range('12/2/2011', '12/5/2011')
    rng2._data.freq = BDay()
    result = rng1.union(rng2)
    assert isinstance(result, DatetimeIndex)