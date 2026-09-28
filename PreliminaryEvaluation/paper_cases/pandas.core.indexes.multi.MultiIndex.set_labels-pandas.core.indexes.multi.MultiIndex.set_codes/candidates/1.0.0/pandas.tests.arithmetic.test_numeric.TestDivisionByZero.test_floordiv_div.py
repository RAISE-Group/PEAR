def test_floordiv_div(self):
    ser = Series([-1, 0, 1], name='first')
    result = ser // 0
    expected = Series([-np.inf, np.nan, np.inf], name='first')
    tm.assert_series_equal(result, expected)