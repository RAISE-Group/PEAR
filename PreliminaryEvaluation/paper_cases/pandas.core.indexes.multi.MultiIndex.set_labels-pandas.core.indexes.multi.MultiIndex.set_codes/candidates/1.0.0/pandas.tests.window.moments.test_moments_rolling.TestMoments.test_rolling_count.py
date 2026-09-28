def test_rolling_count(self, raw):
    counter = lambda x: np.isfinite(x).astype(float).sum()
    self._check_moment_func(counter, name='count', has_min_periods=False, fill_value=0, raw=raw)