@td.skip_if_no_scipy
def test_cmov_window_corner(self):
    vals = pd.Series([np.nan] * 10)
    result = vals.rolling(5, center=True, win_type='boxcar').mean()
    assert np.isnan(result).all()
    vals = pd.Series([], dtype=object)
    result = vals.rolling(5, center=True, win_type='boxcar').mean()
    assert len(result) == 0
    vals = pd.Series(np.random.randn(5))
    result = vals.rolling(10, win_type='boxcar').mean()
    assert np.isnan(result).all()
    assert len(result) == 5