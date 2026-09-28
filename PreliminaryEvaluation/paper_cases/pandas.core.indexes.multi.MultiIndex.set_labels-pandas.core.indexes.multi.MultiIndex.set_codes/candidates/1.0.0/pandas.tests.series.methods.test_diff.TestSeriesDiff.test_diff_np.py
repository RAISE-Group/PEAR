def test_diff_np(self):
    pytest.skip('skipping due to Series no longer being an ndarray')
    s = Series(np.arange(5))
    r = np.diff(s)
    tm.assert_series_equal(Series([np.nan, 0, 0, 0, np.nan]), r)