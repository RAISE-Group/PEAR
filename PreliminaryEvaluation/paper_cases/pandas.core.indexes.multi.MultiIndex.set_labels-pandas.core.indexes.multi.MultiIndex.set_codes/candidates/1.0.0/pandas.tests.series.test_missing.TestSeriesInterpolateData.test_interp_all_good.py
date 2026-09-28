@td.skip_if_no_scipy
def test_interp_all_good(self):
    s = Series([1, 2, 3])
    result = s.interpolate(method='polynomial', order=1)
    tm.assert_series_equal(result, s)
    result = s.interpolate()
    tm.assert_series_equal(result, s)