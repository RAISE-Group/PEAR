def test_nanvar_axis(self):
    samples_norm = self.samples
    samples_unif = self.prng.uniform(size=samples_norm.shape[0])
    samples = np.vstack([samples_norm, samples_unif])
    actual_variance = nanops.nanvar(samples, axis=1)
    tm.assert_almost_equal(actual_variance, np.array([self.variance, 1.0 / 12]), check_less_precise=2)