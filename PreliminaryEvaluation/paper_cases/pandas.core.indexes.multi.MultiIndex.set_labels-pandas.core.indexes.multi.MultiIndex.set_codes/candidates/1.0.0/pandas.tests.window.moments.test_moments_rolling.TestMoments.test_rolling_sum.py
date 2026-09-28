def test_rolling_sum(self, raw):
    self._check_moment_func(np.nansum, name='sum', zero_min_periods_equal=False, raw=raw)