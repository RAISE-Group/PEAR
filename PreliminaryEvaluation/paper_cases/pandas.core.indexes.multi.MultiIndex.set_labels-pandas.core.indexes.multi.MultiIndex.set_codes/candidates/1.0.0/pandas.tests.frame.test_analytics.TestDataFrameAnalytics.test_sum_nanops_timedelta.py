def test_sum_nanops_timedelta(self):
    idx = ['a', 'b', 'c']
    df = pd.DataFrame({'a': [0, 0], 'b': [0, np.nan], 'c': [np.nan, np.nan]})
    df2 = df.apply(pd.to_timedelta)
    result = df2.sum()
    expected = pd.Series([0, 0, 0], dtype='m8[ns]', index=idx)
    tm.assert_series_equal(result, expected)
    result = df2.sum(min_count=0)
    tm.assert_series_equal(result, expected)
    result = df2.sum(min_count=1)
    expected = pd.Series([0, 0, np.nan], dtype='m8[ns]', index=idx)
    tm.assert_series_equal(result, expected)