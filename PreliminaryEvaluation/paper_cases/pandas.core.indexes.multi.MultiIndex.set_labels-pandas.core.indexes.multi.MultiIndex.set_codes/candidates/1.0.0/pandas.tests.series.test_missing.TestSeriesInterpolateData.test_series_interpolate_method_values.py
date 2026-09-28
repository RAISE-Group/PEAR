def test_series_interpolate_method_values(self):
    ts = _simple_ts('1/1/2000', '1/20/2000')
    ts[::2] = np.nan
    result = ts.interpolate(method='values')
    exp = ts.interpolate()
    tm.assert_series_equal(result, exp)