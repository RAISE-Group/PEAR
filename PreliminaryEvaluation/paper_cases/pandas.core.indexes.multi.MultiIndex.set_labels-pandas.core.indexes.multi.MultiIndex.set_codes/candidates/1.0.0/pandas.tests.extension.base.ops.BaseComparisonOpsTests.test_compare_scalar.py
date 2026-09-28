def test_compare_scalar(self, data, all_compare_operators):
    op_name = all_compare_operators
    s = pd.Series(data)
    self._compare_other(s, data, op_name, 0)