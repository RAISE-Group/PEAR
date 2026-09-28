def test_arith_series_with_scalar(self, data, all_arithmetic_operators):
    op = all_arithmetic_operators
    s = pd.Series(data)
    self._check_op(s, op, 1, exc=TypeError)