def test_axis_aliases(self, float_frame):
    f = float_frame
    expected = f.sum(axis=0)
    result = f.sum(axis='index')
    tm.assert_series_equal(result, expected)
    expected = f.sum(axis=1)
    result = f.sum(axis='columns')
    tm.assert_series_equal(result, expected)