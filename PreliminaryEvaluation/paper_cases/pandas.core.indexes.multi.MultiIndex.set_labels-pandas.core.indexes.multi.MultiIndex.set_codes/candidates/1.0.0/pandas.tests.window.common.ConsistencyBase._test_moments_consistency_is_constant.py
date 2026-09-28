def _test_moments_consistency_is_constant(self, min_periods, count, mean, corr):
    for x, is_constant, no_nans in self.data:
        count_x = count(x)
        mean_x = mean(x)
        corr_x_x = corr(x, x)
        if is_constant:
            exp = x.max() if isinstance(x, Series) else x.max().max()
            expected = x * np.nan
            expected[count_x >= max(min_periods, 1)] = exp
            tm.assert_equal(mean_x, expected)
            expected[:] = np.nan
            tm.assert_equal(corr_x_x, expected)