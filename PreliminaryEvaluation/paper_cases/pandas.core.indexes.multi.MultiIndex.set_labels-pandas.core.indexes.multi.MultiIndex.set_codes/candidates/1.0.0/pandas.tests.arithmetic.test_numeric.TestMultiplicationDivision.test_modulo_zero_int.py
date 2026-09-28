def test_modulo_zero_int(self):
    with np.errstate(all='ignore'):
        s = Series([0, 1])
        result = s % 0
        expected = Series([np.nan, np.nan])
        tm.assert_series_equal(result, expected)
        result = 0 % s
        expected = Series([np.nan, 0.0])
        tm.assert_series_equal(result, expected)