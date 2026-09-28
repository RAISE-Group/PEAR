@td.skip_if_no_scipy
def test_scipy_compat(self):
    from scipy.stats import rankdata

    def _check(arr):
        mask = ~np.isfinite(arr)
        arr = arr.copy()
        result = libalgos.rank_1d(arr)
        arr[mask] = np.inf
        exp = rankdata(arr)
        exp[mask] = np.nan
        tm.assert_almost_equal(result, exp)
    _check(np.array([np.nan, np.nan, 5.0, 5.0, 5.0, np.nan, 1, 2, 3, np.nan]))
    _check(np.array([4.0, np.nan, 5.0, 5.0, 5.0, np.nan, 1, 2, 4.0, np.nan]))