def test_interp_limit_forward(self):
    s = Series([1, 3, np.nan, np.nan, np.nan, 11])
    expected = Series([1.0, 3.0, 5.0, 7.0, np.nan, 11.0])
    result = s.interpolate(method='linear', limit=2, limit_direction='forward')
    tm.assert_series_equal(result, expected)
    result = s.interpolate(method='linear', limit=2, limit_direction='FORWARD')
    tm.assert_series_equal(result, expected)