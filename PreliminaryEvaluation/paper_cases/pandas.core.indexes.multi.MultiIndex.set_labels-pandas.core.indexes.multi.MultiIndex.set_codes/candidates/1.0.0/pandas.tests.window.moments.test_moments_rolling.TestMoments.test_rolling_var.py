def test_rolling_var(self, raw):
    self._check_moment_func(lambda x: np.var(x, ddof=1), name='var', raw=raw)
    self._check_moment_func(lambda x: np.var(x, ddof=0), name='var', ddof=0, raw=raw)