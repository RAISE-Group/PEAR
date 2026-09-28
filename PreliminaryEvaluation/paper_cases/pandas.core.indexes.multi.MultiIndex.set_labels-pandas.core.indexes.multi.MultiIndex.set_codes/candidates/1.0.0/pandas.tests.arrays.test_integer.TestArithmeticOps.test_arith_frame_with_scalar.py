def test_arith_frame_with_scalar(self, data, all_arithmetic_operators):
    op = all_arithmetic_operators
    df = pd.DataFrame({'A': data})
    self._check_op(df, op, 1, exc=TypeError)