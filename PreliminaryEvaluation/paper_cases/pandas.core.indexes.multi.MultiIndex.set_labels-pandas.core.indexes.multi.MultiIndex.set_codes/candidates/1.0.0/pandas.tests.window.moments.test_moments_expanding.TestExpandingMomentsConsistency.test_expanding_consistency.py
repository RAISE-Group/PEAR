@pytest.mark.slow
@pytest.mark.parametrize('min_periods', [0, 1, 2, 3, 4])
def test_expanding_consistency(self, min_periods):
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', message='.*(empty slice|0 for slice).*', category=RuntimeWarning)
        self._test_moments_consistency_mock_mean(mean=lambda x: x.expanding(min_periods=min_periods).mean(), mock_mean=lambda x: x.expanding(min_periods=min_periods).sum() / x.expanding().count())
        self._test_moments_consistency_is_constant(min_periods=min_periods, count=lambda x: x.expanding().count(), mean=lambda x: x.expanding(min_periods=min_periods).mean(), corr=lambda x, y: x.expanding(min_periods=min_periods).corr(y))
        self._test_moments_consistency_var_debiasing_factors(var_unbiased=lambda x: x.expanding(min_periods=min_periods).var(), var_biased=lambda x: x.expanding(min_periods=min_periods).var(ddof=0), var_debiasing_factors=lambda x: x.expanding().count() / (x.expanding().count() - 1.0).replace(0.0, np.nan))
        self._test_moments_consistency(min_periods=min_periods, count=lambda x: x.expanding(min_periods=min_periods).count(), mean=lambda x: x.expanding(min_periods=min_periods).mean(), corr=lambda x, y: x.expanding(min_periods=min_periods).corr(y), var_unbiased=lambda x: x.expanding(min_periods=min_periods).var(), std_unbiased=lambda x: x.expanding(min_periods=min_periods).std(), cov_unbiased=lambda x, y: x.expanding(min_periods=min_periods).cov(y), var_biased=lambda x: x.expanding(min_periods=min_periods).var(ddof=0), std_biased=lambda x: x.expanding(min_periods=min_periods).std(ddof=0), cov_biased=lambda x, y: x.expanding(min_periods=min_periods).cov(y, ddof=0))
        for x, is_constant, no_nans in self.data:
            functions = self.base_functions
            if no_nans:
                functions = self.base_functions + self.no_nan_functions
            for f, require_min_periods, name in functions:
                expanding_f = getattr(x.expanding(min_periods=min_periods), name)
                if require_min_periods and min_periods is not None and (min_periods < require_min_periods):
                    continue
                if name == 'count':
                    expanding_f_result = expanding_f()
                    expanding_apply_f_result = x.expanding(min_periods=0).apply(func=f, raw=True)
                else:
                    if name in ['cov', 'corr']:
                        expanding_f_result = expanding_f(pairwise=False)
                    else:
                        expanding_f_result = expanding_f()
                    expanding_apply_f_result = x.expanding(min_periods=min_periods).apply(func=f, raw=True)
                if name in ['sum', 'prod']:
                    tm.assert_equal(expanding_f_result, expanding_apply_f_result)