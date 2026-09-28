def test_nanvar_all_finite(self):
    samples = self.samples
    actual_variance = nanops.nanvar(samples)
    tm.assert_almost_equal(actual_variance, self.variance, check_less_precise=2)