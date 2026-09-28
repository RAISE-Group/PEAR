def test_timedelta_mode(self):
    exp = Series(['-1 days', '0 days', '1 days'], dtype='timedelta64[ns]')
    s = Series(['1 days', '-1 days', '0 days'], dtype='timedelta64[ns]')
    tm.assert_series_equal(algos.mode(s), exp)
    exp = Series(['2 min', '1 day'], dtype='timedelta64[ns]')
    s = Series(['1 day', '1 day', '-1 day', '-1 day 2 min', '2 min', '2 min'], dtype='timedelta64[ns]')
    tm.assert_series_equal(algos.mode(s), exp)