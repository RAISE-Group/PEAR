def test_fillna_inplace(self):
    x = Series([np.nan, 1.0, np.nan, 3.0, np.nan], ['z', 'a', 'b', 'c', 'd'])
    y = x.copy()
    y.fillna(value=0, inplace=True)
    expected = x.fillna(value=0)
    tm.assert_series_equal(y, expected)