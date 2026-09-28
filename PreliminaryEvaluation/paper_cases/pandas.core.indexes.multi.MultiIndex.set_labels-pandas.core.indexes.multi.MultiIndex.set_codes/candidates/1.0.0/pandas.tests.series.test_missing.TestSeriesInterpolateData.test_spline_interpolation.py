@td.skip_if_no_scipy
def test_spline_interpolation(self):
    s = Series(np.arange(10) ** 2)
    s[np.random.randint(0, 9, 3)] = np.nan
    result1 = s.interpolate(method='spline', order=1)
    expected1 = s.interpolate(method='spline', order=1)
    tm.assert_series_equal(result1, expected1)