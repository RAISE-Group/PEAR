def test_arith_series_with_scalar(self, data, all_arithmetic_operators):
    op_name = all_arithmetic_operators
    s = pd.Series(data)
    self.check_opname(s, op_name, s.iloc[0], exc=self.series_scalar_exc)