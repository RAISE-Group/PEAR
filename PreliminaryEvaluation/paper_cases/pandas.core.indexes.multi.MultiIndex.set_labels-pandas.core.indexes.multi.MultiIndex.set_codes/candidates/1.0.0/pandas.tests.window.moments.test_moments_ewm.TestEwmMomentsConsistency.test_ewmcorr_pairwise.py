def test_ewmcorr_pairwise(self):
    self._check_pairwise_moment('ewm', 'corr', span=10, min_periods=5)