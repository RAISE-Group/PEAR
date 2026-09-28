def test_rolling_median(self, raw):
    self._check_moment_func(np.median, name='median', raw=raw)