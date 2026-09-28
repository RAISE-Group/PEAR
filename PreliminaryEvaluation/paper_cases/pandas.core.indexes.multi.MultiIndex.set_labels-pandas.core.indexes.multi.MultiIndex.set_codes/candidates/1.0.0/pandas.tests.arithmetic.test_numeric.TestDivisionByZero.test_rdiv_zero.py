def test_rdiv_zero(self):
    ser = Series([-1, 0, 1], name='first')
    expected = Series([0.0, np.nan, 0.0], name='first')
    result = 0 / ser
    tm.assert_series_equal(result, expected)