@td.skip_if_no_scipy
def test_rolling_skew(self, raw):
    from scipy.stats import skew
    self._check_moment_func(lambda x: skew(x, bias=False), name='skew', raw=raw)