def test_interp_limit_no_nans(self):
    s = pd.Series([1.0, 2.0, 3.0])
    result = s.interpolate(limit=1)
    expected = s
    tm.assert_series_equal(result, expected)