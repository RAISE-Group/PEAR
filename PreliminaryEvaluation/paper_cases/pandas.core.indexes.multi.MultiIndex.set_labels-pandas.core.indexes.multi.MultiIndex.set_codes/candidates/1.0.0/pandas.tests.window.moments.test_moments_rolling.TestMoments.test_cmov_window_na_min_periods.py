@td.skip_if_no_scipy
def test_cmov_window_na_min_periods(self):
    vals = Series(np.random.randn(10))
    vals[4] = np.nan
    vals[8] = np.nan
    xp = vals.rolling(5, min_periods=4, center=True).mean()
    rs = vals.rolling(5, win_type='boxcar', min_periods=4, center=True).mean()
    tm.assert_series_equal(xp, rs)