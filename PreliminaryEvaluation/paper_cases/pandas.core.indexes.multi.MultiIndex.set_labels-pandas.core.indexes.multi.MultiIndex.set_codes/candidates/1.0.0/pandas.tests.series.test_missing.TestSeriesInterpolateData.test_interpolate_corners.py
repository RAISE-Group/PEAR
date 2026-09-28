@pytest.mark.parametrize('kwargs', [{}, pytest.param({'method': 'polynomial', 'order': 1}, marks=td.skip_if_no_scipy)])
def test_interpolate_corners(self, kwargs):
    s = Series([np.nan, np.nan])
    tm.assert_series_equal(s.interpolate(**kwargs), s)
    s = Series([], dtype=object).interpolate()
    tm.assert_series_equal(s.interpolate(**kwargs), s)