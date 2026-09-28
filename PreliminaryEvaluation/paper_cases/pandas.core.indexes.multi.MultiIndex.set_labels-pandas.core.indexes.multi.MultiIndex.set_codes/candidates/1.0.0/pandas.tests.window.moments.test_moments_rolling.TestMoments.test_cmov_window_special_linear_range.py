@td.skip_if_no_scipy
def test_cmov_window_special_linear_range(self, win_types_special):
    kwds = {'kaiser': {'beta': 1.0}, 'gaussian': {'std': 1.0}, 'general_gaussian': {'power': 2.0, 'width': 2.0}, 'slepian': {'width': 0.5}, 'exponential': {'tau': 10}}
    vals = np.array(range(10), dtype=np.float)
    xp = vals.copy()
    xp[:2] = np.nan
    xp[-2:] = np.nan
    xp = Series(xp)
    rs = Series(vals).rolling(5, win_type=win_types_special, center=True).mean(**kwds[win_types_special])
    tm.assert_series_equal(xp, rs)