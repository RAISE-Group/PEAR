def _test_moments_consistency(self, min_periods, count, mean, corr, var_unbiased=None, std_unbiased=None, cov_unbiased=None, var_biased=None, std_biased=None, cov_biased=None):
    for x, is_constant, no_nans in self.data:
        count_x = count(x)
        mean_x = mean(x)
        for std, var, cov in [(std_biased, var_biased, cov_biased), (std_unbiased, var_unbiased, cov_unbiased)]:
            var_x = var(x)
            std_x = std(x)
            assert not (var_x < 0).any().any()
            assert not (std_x < 0).any().any()
            if cov:
                cov_x_x = cov(x, x)
                assert not (cov_x_x < 0).any().any()
                tm.assert_equal(var_x, cov_x_x)
            tm.assert_equal(var_x, std_x * std_x)
            if var is var_biased:
                mean_x2 = mean(x * x)
                tm.assert_equal(var_x, mean_x2 - mean_x * mean_x)
            if is_constant:
                assert not (var_x > 0).any().any()
                expected = x * np.nan
                expected[count_x >= max(min_periods, 1)] = 0.0
                if var is var_unbiased:
                    expected[count_x < 2] = np.nan
                tm.assert_equal(var_x, expected)
            if isinstance(x, Series):
                for y, is_constant, no_nans in self.data:
                    if not x.isna().equals(y.isna()):
                        continue
                    corr_x_y = corr(x, y)
                    corr_y_x = corr(y, x)
                    tm.assert_equal(corr_x_y, corr_y_x)
                    if cov:
                        cov_x_y = cov(x, y)
                        cov_y_x = cov(y, x)
                        tm.assert_equal(cov_x_y, cov_y_x)
                        var_x_plus_y = var(x + y)
                        var_y = var(y)
                        tm.assert_equal(cov_x_y, 0.5 * (var_x_plus_y - var_x - var_y))
                        std_y = std(y)
                        tm.assert_equal(corr_x_y, cov_x_y / (std_x * std_y))
                        if cov is cov_biased:
                            mean_y = mean(y)
                            mean_x_times_y = mean(x * y)
                            tm.assert_equal(cov_x_y, mean_x_times_y - mean_x * mean_y)