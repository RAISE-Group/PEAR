def test_logical_operators_int_dtype_with_int_scalar(self):
    s_0123 = Series(range(4), dtype='int64')
    res = s_0123 & 0
    expected = Series([0] * 4)
    tm.assert_series_equal(res, expected)
    res = s_0123 & 1
    expected = Series([0, 1, 0, 1])
    tm.assert_series_equal(res, expected)