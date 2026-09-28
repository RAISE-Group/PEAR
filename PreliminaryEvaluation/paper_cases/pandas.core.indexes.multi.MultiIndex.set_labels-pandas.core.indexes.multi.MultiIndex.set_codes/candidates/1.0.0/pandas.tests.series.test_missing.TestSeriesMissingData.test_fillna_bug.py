def test_fillna_bug(self):
    x = Series([np.nan, 1.0, np.nan, 3.0, np.nan], ['z', 'a', 'b', 'c', 'd'])
    filled = x.fillna(method='ffill')
    expected = Series([np.nan, 1.0, 1.0, 3.0, 3.0], x.index)
    tm.assert_series_equal(filled, expected)
    filled = x.fillna(method='bfill')
    expected = Series([1.0, 1.0, 3.0, 3.0, np.nan], x.index)
    tm.assert_series_equal(filled, expected)