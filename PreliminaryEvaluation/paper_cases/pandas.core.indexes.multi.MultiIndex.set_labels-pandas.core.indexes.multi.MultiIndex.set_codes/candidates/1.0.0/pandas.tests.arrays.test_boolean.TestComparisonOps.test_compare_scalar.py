def test_compare_scalar(self, data, all_compare_operators):
    op_name = all_compare_operators
    self._compare_other(data, op_name, True)