def test_convert_non_ns(self):
    arr = np.array([1, 2, 3], dtype='timedelta64[s]')
    s = Series(arr)
    expected = Series(pd.timedelta_range('00:00:01', periods=3, freq='s'))
    tm.assert_series_equal(s, expected)
    s = Series(np.array(['2013-01-01', '2013-01-02', '2013-01-03'], dtype='datetime64[D]'))
    tm.assert_series_equal(s, Series(date_range('20130101', periods=3, freq='D')))