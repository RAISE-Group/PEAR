def test_div_zero_inf_signs(self):
    ser = Series([-1, 0, 1], name='first')
    expected = Series([-np.inf, np.nan, np.inf], name='first')
    result = ser / 0
    tm.assert_series_equal(result, expected)