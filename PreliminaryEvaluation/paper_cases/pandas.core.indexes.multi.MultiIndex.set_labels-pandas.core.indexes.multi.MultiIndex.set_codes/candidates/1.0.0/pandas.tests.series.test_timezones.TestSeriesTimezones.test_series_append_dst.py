def test_series_append_dst(self):
    rng1 = date_range('1/1/2016 01:00', periods=3, freq='H', tz='US/Eastern')
    rng2 = date_range('8/1/2016 01:00', periods=3, freq='H', tz='US/Eastern')
    ser1 = Series([1, 2, 3], index=rng1)
    ser2 = Series([10, 11, 12], index=rng2)
    ts_result = ser1.append(ser2)
    exp_index = DatetimeIndex(['2016-01-01 01:00', '2016-01-01 02:00', '2016-01-01 03:00', '2016-08-01 01:00', '2016-08-01 02:00', '2016-08-01 03:00'], tz='US/Eastern')
    exp = Series([1, 2, 3, 10, 11, 12], index=exp_index)
    tm.assert_series_equal(ts_result, exp)
    assert ts_result.index.tz == rng1.tz