def test_logical_operators_int_dtype_with_bool(self):
    s_0123 = Series(range(4), dtype='int64')
    expected = Series([False] * 4)
    result = s_0123 & False
    tm.assert_series_equal(result, expected)
    result = s_0123 & [False]
    tm.assert_series_equal(result, expected)
    result = s_0123 & (False,)
    tm.assert_series_equal(result, expected)
    result = s_0123 ^ False
    expected = Series([False, True, True, True])
    tm.assert_series_equal(result, expected)