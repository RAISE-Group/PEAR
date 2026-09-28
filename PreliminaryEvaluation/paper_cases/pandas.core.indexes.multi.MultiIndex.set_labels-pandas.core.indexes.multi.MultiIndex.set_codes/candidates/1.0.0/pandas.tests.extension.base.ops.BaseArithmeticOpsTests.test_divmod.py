def test_divmod(self, data):
    s = pd.Series(data)
    self._check_divmod_op(s, divmod, 1, exc=self.divmod_exc)
    self._check_divmod_op(1, ops.rdivmod, s, exc=self.divmod_exc)