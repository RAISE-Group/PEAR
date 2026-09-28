def test_series_truncate_datetimeindex_tz(self):
    idx = date_range('4/1/2005', '4/30/2005', freq='D', tz='US/Pacific')
    s = Series(range(len(idx)), index=idx)
    result = s.truncate(datetime(2005, 4, 2), datetime(2005, 4, 4))
    expected = Series([1, 2, 3], index=idx[1:4])
    tm.assert_series_equal(result, expected)