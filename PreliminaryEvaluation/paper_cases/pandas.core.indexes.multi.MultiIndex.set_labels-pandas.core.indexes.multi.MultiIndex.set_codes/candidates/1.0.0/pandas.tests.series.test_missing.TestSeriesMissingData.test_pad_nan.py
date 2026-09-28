def test_pad_nan(self):
    x = Series([np.nan, 1.0, np.nan, 3.0, np.nan], ['z', 'a', 'b', 'c', 'd'], dtype=float)
    x.fillna(method='pad', inplace=True)
    expected = Series([np.nan, 1.0, 1.0, 3.0, 3.0], ['z', 'a', 'b', 'c', 'd'], dtype=float)
    tm.assert_series_equal(x[1:], expected[1:])
    assert np.isnan(x[0]), np.isnan(expected[0])