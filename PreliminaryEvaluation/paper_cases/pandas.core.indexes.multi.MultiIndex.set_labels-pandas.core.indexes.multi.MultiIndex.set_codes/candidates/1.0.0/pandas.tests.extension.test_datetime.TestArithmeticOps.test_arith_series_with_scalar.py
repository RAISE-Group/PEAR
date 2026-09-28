def test_arith_series_with_scalar(self, data, all_arithmetic_operators):
    if all_arithmetic_operators in self.implements:
        s = pd.Series(data)
        self.check_opname(s, all_arithmetic_operators, s.iloc[0], exc=None)
    else:
        super().test_arith_series_with_scalar(data, all_arithmetic_operators)