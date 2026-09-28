def test_ops_series(self):
    td = Timedelta('1 day')
    other = pd.Series([1, 2])
    expected = pd.Series(pd.to_timedelta(['1 day', '2 days']))
    tm.assert_series_equal(expected, td * other)
    tm.assert_series_equal(expected, other * td)