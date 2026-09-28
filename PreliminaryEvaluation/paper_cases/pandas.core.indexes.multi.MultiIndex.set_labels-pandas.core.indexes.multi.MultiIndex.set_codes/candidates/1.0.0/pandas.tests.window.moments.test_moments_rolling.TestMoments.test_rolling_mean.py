def test_rolling_mean(self, raw):
    self._check_moment_func(np.mean, name='mean', raw=raw)