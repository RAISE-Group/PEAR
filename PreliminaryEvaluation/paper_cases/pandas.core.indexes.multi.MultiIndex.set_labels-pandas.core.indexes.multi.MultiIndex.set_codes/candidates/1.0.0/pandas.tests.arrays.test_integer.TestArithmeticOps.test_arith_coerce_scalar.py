def test_arith_coerce_scalar(self, data, all_arithmetic_operators):
    op = all_arithmetic_operators
    s = pd.Series(data)
    other = 0.01
    self._check_op(s, op, other)