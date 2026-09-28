@td.skip_if_no_scipy
def test_rolling_kurt(self, raw):
    from scipy.stats import kurtosis
    self._check_moment_func(lambda x: kurtosis(x, bias=False), name='kurt', raw=raw)