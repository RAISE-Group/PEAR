def _test_moments_consistency_var_debiasing_factors(self, var_biased=None, var_unbiased=None, var_debiasing_factors=None):
    for x, is_constant, no_nans in self.data:
        if var_unbiased and var_biased and var_debiasing_factors:
            var_unbiased_x = var_unbiased(x)
            var_biased_x = var_biased(x)
            var_debiasing_factors_x = var_debiasing_factors(x)
            tm.assert_equal(var_unbiased_x, var_biased_x * var_debiasing_factors_x)