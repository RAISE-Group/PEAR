def test_nan_irregular_index(self):
    s = Series([1, 2, np.nan, 4], index=[1, 3, 5, 9])
    result = s.interpolate()
    expected = Series([1.0, 2.0, 3.0, 4.0], index=[1, 3, 5, 9])
    tm.assert_series_equal(result, expected)