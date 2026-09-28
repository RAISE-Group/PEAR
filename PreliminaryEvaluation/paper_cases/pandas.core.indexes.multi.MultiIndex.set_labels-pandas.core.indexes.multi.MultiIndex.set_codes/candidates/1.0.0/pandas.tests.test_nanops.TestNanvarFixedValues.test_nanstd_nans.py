def test_nanstd_nans(self):
    samples = np.nan * np.ones(2 * self.samples.shape[0])
    samples[::2] = self.samples
    actual_std = nanops.nanstd(samples, skipna=True)
    tm.assert_almost_equal(actual_std, self.variance ** 0.5, check_less_precise=2)
    actual_std = nanops.nanvar(samples, skipna=False)
    tm.assert_almost_equal(actual_std, np.nan, check_less_precise=2)