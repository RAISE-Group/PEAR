def test_rolling_cov_pairwise(self):
    self._check_pairwise_moment('rolling', 'cov', window=10, min_periods=5)