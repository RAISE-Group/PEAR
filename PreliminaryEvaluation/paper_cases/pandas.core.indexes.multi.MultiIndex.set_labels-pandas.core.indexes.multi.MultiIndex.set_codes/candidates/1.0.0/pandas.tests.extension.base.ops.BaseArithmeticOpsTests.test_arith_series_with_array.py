def test_arith_series_with_array(self, data, all_arithmetic_operators):
    op_name = all_arithmetic_operators
    s = pd.Series(data)
    self.check_opname(s, op_name, pd.Series([s.iloc[0]] * len(s)), exc=self.series_array_exc)