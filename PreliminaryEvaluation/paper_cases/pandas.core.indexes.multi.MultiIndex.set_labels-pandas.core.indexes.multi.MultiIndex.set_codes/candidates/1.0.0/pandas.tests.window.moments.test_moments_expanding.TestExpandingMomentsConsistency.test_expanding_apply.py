@pytest.mark.parametrize('has_min_periods', [True, False])
def test_expanding_apply(self, raw, has_min_periods):

    def expanding_mean(x, min_periods=1):
        exp = x.expanding(min_periods=min_periods)
        result = exp.apply(lambda x: x.mean(), raw=raw)
        return result
    self._check_expanding(expanding_mean, np.mean, preserve_nan=False)
    self._check_expanding_has_min_periods(expanding_mean, np.mean, has_min_periods)