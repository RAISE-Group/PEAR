def test_prod(self):
    string_series = tm.makeStringSeries().rename('series')
    self._check_stat_op('prod', np.prod, string_series)