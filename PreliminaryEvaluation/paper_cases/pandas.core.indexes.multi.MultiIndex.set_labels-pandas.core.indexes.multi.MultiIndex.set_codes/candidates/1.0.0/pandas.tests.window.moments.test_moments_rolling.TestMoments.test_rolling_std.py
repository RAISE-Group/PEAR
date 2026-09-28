def test_rolling_std(self, raw):
    self._check_moment_func(lambda x: np.std(x, ddof=1), name='std', raw=raw)
    self._check_moment_func(lambda x: np.std(x, ddof=0), name='std', ddof=0, raw=raw)