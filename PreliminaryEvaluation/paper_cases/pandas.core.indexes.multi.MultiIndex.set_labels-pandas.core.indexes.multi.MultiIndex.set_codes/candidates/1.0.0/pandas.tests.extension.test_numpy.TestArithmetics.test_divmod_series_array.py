def test_divmod_series_array(self, data):
    s = pd.Series(data)
    self._check_divmod_op(s, divmod, data, exc=None)