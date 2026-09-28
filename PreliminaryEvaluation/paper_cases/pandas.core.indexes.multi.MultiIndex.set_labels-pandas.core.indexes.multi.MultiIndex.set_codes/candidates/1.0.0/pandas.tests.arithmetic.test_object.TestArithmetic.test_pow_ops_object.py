def test_pow_ops_object(self):
    a = Series([1, np.nan, 1, np.nan], dtype=object)
    b = Series([1, np.nan, np.nan, 1], dtype=object)
    result = a ** b
    expected = Series(a.values ** b.values, dtype=object)
    tm.assert_series_equal(result, expected)
    result = b ** a
    expected = Series(b.values ** a.values, dtype=object)
    tm.assert_series_equal(result, expected)