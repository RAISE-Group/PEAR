def test_date_range_localize(self):
    rng = date_range('3/11/2012 03:00', periods=15, freq='H', tz='US/Eastern')
    rng2 = DatetimeIndex(['3/11/2012 03:00', '3/11/2012 04:00'], tz='US/Eastern')
    rng3 = date_range('3/11/2012 03:00', periods=15, freq='H')
    rng3 = rng3.tz_localize('US/Eastern')
    tm.assert_index_equal(rng, rng3)
    val = rng[0]
    exp = Timestamp('3/11/2012 03:00', tz='US/Eastern')
    assert val.hour == 3
    assert exp.hour == 3
    assert val == exp
    tm.assert_index_equal(rng[:2], rng2)
    rng = date_range('3/11/2012 00:00', periods=2, freq='H', tz='US/Eastern')
    rng2 = DatetimeIndex(['3/11/2012 00:00', '3/11/2012 01:00'], tz='US/Eastern')
    tm.assert_index_equal(rng, rng2)
    exp = Timestamp('3/11/2012 00:00', tz='US/Eastern')
    assert exp.hour == 0
    assert rng[0] == exp
    exp = Timestamp('3/11/2012 01:00', tz='US/Eastern')
    assert exp.hour == 1
    assert rng[1] == exp
    rng = date_range('3/11/2012 00:00', periods=10, freq='H', tz='US/Eastern')
    assert rng[2].hour == 3