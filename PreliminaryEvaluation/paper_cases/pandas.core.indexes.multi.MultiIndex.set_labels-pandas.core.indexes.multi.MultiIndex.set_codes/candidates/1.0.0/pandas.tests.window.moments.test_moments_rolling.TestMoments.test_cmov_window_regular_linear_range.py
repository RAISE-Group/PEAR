@td.skip_if_no_scipy
def test_cmov_window_regular_linear_range(self, win_types):
    vals = np.array(range(10), dtype=np.float)
    xp = vals.copy()
    xp[:2] = np.nan
    xp[-2:] = np.nan
    xp = Series(xp)
    rs = Series(vals).rolling(5, win_type=win_types, center=True).mean()
    tm.assert_series_equal(xp, rs)