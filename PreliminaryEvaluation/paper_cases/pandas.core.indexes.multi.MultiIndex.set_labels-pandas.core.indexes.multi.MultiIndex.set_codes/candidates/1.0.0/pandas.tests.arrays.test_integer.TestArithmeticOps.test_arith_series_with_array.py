def test_arith_series_with_array(self, data, all_arithmetic_operators):
    op = all_arithmetic_operators
    s = pd.Series(data)
    other = np.ones(len(s), dtype=s.dtype.type)
    self._check_op(s, op, other, exc=TypeError)