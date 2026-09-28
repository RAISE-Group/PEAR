def test_diff_object_dtype(self):
    s = Series([False, True, 5.0, np.nan, True, False])
    result = s.diff()
    expected = s - s.shift(1)
    tm.assert_series_equal(result, expected)