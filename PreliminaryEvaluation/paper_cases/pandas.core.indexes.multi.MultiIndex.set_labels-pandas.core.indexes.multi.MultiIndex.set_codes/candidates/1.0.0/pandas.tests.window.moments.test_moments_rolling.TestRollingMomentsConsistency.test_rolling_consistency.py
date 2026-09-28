@pytest.mark.slow
@pytest.mark.parametrize('window,min_periods,center', list(_rolling_consistency_cases()))
def test_rolling_consistency(self, window, min_periods, center):
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', message='.*(empty slice|0 for slice).*', category=RuntimeWarning)
        self._test_moments_consistency_mock_mean(mean=lambda x: x.rolling(window=window, min_periods=min_periods, center=center).mean(), mock_mean=lambda x: x.rolling(window=window, min_periods=min_periods, center=center).sum().divide(x.rolling(window=window, min_periods=min_periods, center=center).count()))
        self._test_moments_consistency_is_constant(min_periods=min_periods, count=lambda x: x.rolling(window=window, min_periods=min_periods, center=center).count(), mean=lambda x: x.rolling(window=window, min_periods=min_periods, center=center).mean(), corr=lambda x, y: x.rolling(window=window, min_periods=min_periods, center=center).corr(y))
        self._test_moments_consistency_var_debiasing_factors(var_unbiased=lambda x: x.rolling(window=window, min_periods=min_periods, center=center).var(), var_biased=lambda x: x.rolling(window=window, min_periods=min_periods, center=center).var(ddof=0), var_debiasing_factors=lambda x: x.rolling(window=window, min_periods=min_periods, center=center).count().divide((x.rolling(window=window, min_periods=min_periods, center=center).count() - 1.0).replace(0.0, np.nan)))
        self._test_moments_consistency(min_periods=min_periods, count=lambda x: x.rolling(window=window, min_periods=min_periods, center=center).count(), mean=lambda x: x.rolling(window=window, min_periods=min_periods, center=center).mean(), corr=lambda x, y: x.rolling(window=window, min_periods=min_periods, center=center).corr(y), var_unbiased=lambda x: x.rolling(window=window, min_periods=min_periods, center=center).var(), std_unbiased=lambda x: x.rolling(window=window, min_periods=min_periods, center=center).std(), cov_unbiased=lambda x, y: x.rolling(window=window, min_periods=min_periods, center=center).cov(y), var_biased=lambda x: x.rolling(window=window, min_periods=min_periods, center=center).var(ddof=0), std_biased=lambda x: x.rolling(window=window, min_periods=min_periods, center=center).std(ddof=0), cov_biased=lambda x, y: x.rolling(window=window, min_periods=min_periods, center=center).cov(y, ddof=0))
        for x, is_constant, no_nans in self.data:
            functions = self.base_functions
            if no_nans:
                functions = self.base_functions + self.no_nan_functions
            for f, require_min_periods, name in functions:
                rolling_f = getattr(x.rolling(window=window, center=center, min_periods=min_periods), name)
                if require_min_periods and min_periods is not None and (min_periods < require_min_periods):
                    continue
                if name == 'count':
                    rolling_f_result = rolling_f()
                    rolling_apply_f_result = x.rolling(window=window, min_periods=min_periods, center=center).apply(func=f, raw=True)
                else:
                    if name in ['cov', 'corr']:
                        rolling_f_result = rolling_f(pairwise=False)
                    else:
                        rolling_f_result = rolling_f()
                    rolling_apply_f_result = x.rolling(window=window, min_periods=min_periods, center=center).apply(func=f, raw=True)
                if name in ['sum', 'prod']:
                    tm.assert_equal(rolling_f_result, rolling_apply_f_result)