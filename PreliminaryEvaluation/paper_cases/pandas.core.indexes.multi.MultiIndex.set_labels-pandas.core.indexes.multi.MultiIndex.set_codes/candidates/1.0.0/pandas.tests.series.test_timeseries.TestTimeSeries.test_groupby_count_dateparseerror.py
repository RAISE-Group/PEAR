def test_groupby_count_dateparseerror(self):
    dr = date_range(start='1/1/2012', freq='5min', periods=10)
    s = Series(np.arange(10), index=[dr, np.arange(10)])
    grouped = s.groupby(lambda x: x[1] % 2 == 0)
    result = grouped.count()
    s = Series(np.arange(10), index=[np.arange(10), dr])
    grouped = s.groupby(lambda x: x[0] % 2 == 0)
    expected = grouped.count()
    tm.assert_series_equal(result, expected)