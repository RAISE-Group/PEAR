def test_nanvar_ddof(self):
    n = 5
    samples = self.prng.uniform(size=(10000, n + 1))
    samples[:, -1] = np.nan
    variance_0 = nanops.nanvar(samples, axis=1, skipna=True, ddof=0).mean()
    variance_1 = nanops.nanvar(samples, axis=1, skipna=True, ddof=1).mean()
    variance_2 = nanops.nanvar(samples, axis=1, skipna=True, ddof=2).mean()
    var = 1.0 / 12
    tm.assert_almost_equal(variance_1, var, check_less_precise=2)
    tm.assert_almost_equal(variance_0, (n - 1.0) / n * var, check_less_precise=2)
    tm.assert_almost_equal(variance_2, (n - 1.0) / (n - 2.0) * var, check_less_precise=2)