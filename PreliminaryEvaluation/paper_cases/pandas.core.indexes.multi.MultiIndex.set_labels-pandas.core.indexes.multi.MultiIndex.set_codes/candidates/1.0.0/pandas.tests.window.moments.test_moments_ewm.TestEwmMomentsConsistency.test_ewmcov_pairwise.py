def test_ewmcov_pairwise(self):
    self._check_pairwise_moment('ewm', 'cov', span=10, min_periods=5)