def test_compare_array(self, data, all_compare_operators):
    op_name = all_compare_operators
    s = pd.Series(data)
    other = pd.Series([data[0]] * len(data))
    self._compare_other(s, data, op_name, other)