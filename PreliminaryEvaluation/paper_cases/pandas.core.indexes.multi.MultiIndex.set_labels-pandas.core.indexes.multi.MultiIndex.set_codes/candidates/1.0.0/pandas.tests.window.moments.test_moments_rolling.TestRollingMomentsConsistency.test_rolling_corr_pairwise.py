def test_rolling_corr_pairwise(self):
    self._check_pairwise_moment('rolling', 'corr', window=10, min_periods=5)