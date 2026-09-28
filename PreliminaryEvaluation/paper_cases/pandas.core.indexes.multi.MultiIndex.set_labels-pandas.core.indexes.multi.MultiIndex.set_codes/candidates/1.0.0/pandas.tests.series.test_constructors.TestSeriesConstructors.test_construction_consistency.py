def test_construction_consistency(self):
    s = Series(pd.date_range('20130101', periods=3, tz='US/Eastern'))
    result = Series(s, dtype=s.dtype)
    tm.assert_series_equal(result, s)
    result = Series(s.dt.tz_convert('UTC'), dtype=s.dtype)
    tm.assert_series_equal(result, s)
    result = Series(s.values, dtype=s.dtype)
    tm.assert_series_equal(result, s)