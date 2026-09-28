def test_divmod_series_array(self, data, data_for_twos):
    s = pd.Series(data)
    self._check_divmod_op(s, divmod, data)
    other = data_for_twos
    self._check_divmod_op(other, ops.rdivmod, s)
    other = pd.Series(other)
    self._check_divmod_op(other, ops.rdivmod, s)