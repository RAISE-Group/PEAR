def test_logical_operators_bool_dtype_with_int(self):
    index = list('bca')
    s_tft = Series([True, False, True], index=index)
    s_fff = Series([False, False, False], index=index)
    res = s_tft & 0
    expected = s_fff
    tm.assert_series_equal(res, expected)
    res = s_tft & 1
    expected = s_tft
    tm.assert_series_equal(res, expected)