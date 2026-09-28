@pytest.mark.slow
@pytest.mark.parametrize('min_periods', [0, 1, 2, 3, 4])
@pytest.mark.parametrize('adjust', [True, False])
@pytest.mark.parametrize('ignore_na', [True, False])
def test_ewm_consistency(self, min_periods, adjust, ignore_na):

    def _weights(s, com, adjust, ignore_na):
        if isinstance(s, DataFrame):
            if not len(s.columns):
                return DataFrame(index=s.index, columns=s.columns)
            w = concat([_weights(s.iloc[:, i], com=com, adjust=adjust, ignore_na=ignore_na) for i, _ in enumerate(s.columns)], axis=1)
            w.index = s.index
            w.columns = s.columns
            return w
        w = Series(np.nan, index=s.index)
        alpha = 1.0 / (1.0 + com)
        if ignore_na:
            w[s.notna()] = _weights(s[s.notna()], com=com, adjust=adjust, ignore_na=False)
        elif adjust:
            for i in range(len(s)):
                if s.iat[i] == s.iat[i]:
                    w.iat[i] = pow(1.0 / (1.0 - alpha), i)
        else:
            sum_wts = 0.0
            prev_i = -1
            for i in range(len(s)):
                if s.iat[i] == s.iat[i]:
                    if prev_i == -1:
                        w.iat[i] = 1.0
                    else:
                        w.iat[i] = alpha * sum_wts / pow(1.0 - alpha, i - prev_i)
                    sum_wts += w.iat[i]
                    prev_i = i
        return w

    def _variance_debiasing_factors(s, com, adjust, ignore_na):
        weights = _weights(s, com=com, adjust=adjust, ignore_na=ignore_na)
        cum_sum = weights.cumsum().fillna(method='ffill')
        cum_sum_sq = (weights * weights).cumsum().fillna(method='ffill')
        numerator = cum_sum * cum_sum
        denominator = numerator - cum_sum_sq
        denominator[denominator <= 0.0] = np.nan
        return numerator / denominator

    def _ewma(s, com, min_periods, adjust, ignore_na):
        weights = _weights(s, com=com, adjust=adjust, ignore_na=ignore_na)
        result = s.multiply(weights).cumsum().divide(weights.cumsum()).fillna(method='ffill')
        result[s.expanding().count() < (max(min_periods, 1) if min_periods else 1)] = np.nan
        return result
    com = 3.0
    self._test_moments_consistency_mock_mean(mean=lambda x: x.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean(), mock_mean=lambda x: _ewma(x, com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na))
    self._test_moments_consistency_is_constant(min_periods=min_periods, count=lambda x: x.expanding().count(), mean=lambda x: x.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean(), corr=lambda x, y: x.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).corr(y))
    self._test_moments_consistency_var_debiasing_factors(var_unbiased=lambda x: x.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).var(bias=False), var_biased=lambda x: x.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).var(bias=True), var_debiasing_factors=lambda x: _variance_debiasing_factors(x, com=com, adjust=adjust, ignore_na=ignore_na))
    self._test_moments_consistency(min_periods=min_periods, count=lambda x: x.expanding().count(), mean=lambda x: x.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean(), corr=lambda x, y: x.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).corr(y), var_unbiased=lambda x: x.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).var(bias=False), std_unbiased=lambda x: x.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).std(bias=False), cov_unbiased=lambda x, y: x.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).cov(y, bias=False), var_biased=lambda x: x.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).var(bias=True), std_biased=lambda x: x.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).std(bias=True), cov_biased=lambda x, y: x.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).cov(y, bias=True))