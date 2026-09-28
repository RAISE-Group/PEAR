@td.skip_if_no_scipy
def test_spline_smooth(self):
    s = Series([1, 2, np.nan, 4, 5.1, np.nan, 7])
    assert s.interpolate(method='spline', order=3, s=0)[5] != s.interpolate(method='spline', order=3)[5]