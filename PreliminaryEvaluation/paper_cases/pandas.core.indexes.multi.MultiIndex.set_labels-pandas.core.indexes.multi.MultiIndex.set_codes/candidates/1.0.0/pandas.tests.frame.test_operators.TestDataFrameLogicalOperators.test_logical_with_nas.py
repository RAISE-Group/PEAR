def test_logical_with_nas(self):
    d = DataFrame({'a': [np.nan, False], 'b': [True, True]})
    result = d['a'] | d['b']
    expected = Series([False, True])
    tm.assert_series_equal(result, expected)
    result = d['a'].fillna(False) | d['b']
    expected = Series([True, True])
    tm.assert_series_equal(result, expected)
    result = d['a'].fillna(False, downcast=False) | d['b']
    expected = Series([True, True])
    tm.assert_series_equal(result, expected)