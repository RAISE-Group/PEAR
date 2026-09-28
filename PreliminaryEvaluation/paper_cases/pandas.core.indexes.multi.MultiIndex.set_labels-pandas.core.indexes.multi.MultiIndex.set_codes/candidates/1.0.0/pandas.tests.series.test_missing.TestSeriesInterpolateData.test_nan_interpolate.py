@pytest.mark.parametrize('kwargs', [{}, pytest.param({'method': 'polynomial', 'order': 1}, marks=td.skip_if_no_scipy)])
def test_nan_interpolate(self, kwargs):
    s = Series([0, 1, np.nan, 3])
    result = s.interpolate(**kwargs)
    expected = Series([0.0, 1.0, 2.0, 3.0])
    tm.assert_series_equal(result, expected)