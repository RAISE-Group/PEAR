def test_constructor_coerce_float_valid(self, float_dtype):
    s = Series([1, 2, 3.5], dtype=float_dtype)
    expected = Series([1, 2, 3.5]).astype(float_dtype)
    tm.assert_series_equal(s, expected)