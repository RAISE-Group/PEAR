def test_arith_integer_array(self, data, all_arithmetic_operators):
    op = all_arithmetic_operators
    s = pd.Series(data)
    rhs = pd.Series([1] * len(data), dtype=data.dtype)
    rhs.iloc[-1] = np.nan
    self._check_op(s, op, rhs)