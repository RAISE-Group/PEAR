def test_nanvar_nans(self):
    samples = np.nan * np.ones(2 * self.samples.shape[0])
    samples[::2] = self.samples
    actual_variance = nanops.nanvar(samples, skipna=True)
    tm.assert_almost_equal(actual_variance, self.variance, check_less_precise=2)
    actual_variance = nanops.nanvar(samples, skipna=False)
    tm.assert_almost_equal(actual_variance, np.nan, check_less_precise=2)