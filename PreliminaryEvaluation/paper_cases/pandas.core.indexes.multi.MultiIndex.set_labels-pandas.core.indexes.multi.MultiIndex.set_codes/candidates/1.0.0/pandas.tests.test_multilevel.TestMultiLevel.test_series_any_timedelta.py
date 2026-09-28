def test_series_any_timedelta(self):
    df = DataFrame({'a': Series([0, 0]), 't': Series([pd.to_timedelta(0, 's'), pd.to_timedelta(1, 'ms')])})
    result = df.any(axis=0)
    expected = Series(data=[False, True], index=['a', 't'])
    tm.assert_series_equal(result, expected)
    result = df.any(axis=1)
    expected = Series(data=[False, True])
    tm.assert_series_equal(result, expected)