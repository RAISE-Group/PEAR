def test_maybe_convert_numeric_post_floatify_nan(self, coerce):
    data = np.array(['1.200', '-999.000', '4.500'], dtype=object)
    expected = np.array([1.2, np.nan, 4.5], dtype=np.float64)
    nan_values = {-999, -999.0}
    out = lib.maybe_convert_numeric(data, nan_values, coerce)
    tm.assert_numpy_array_equal(out, expected)