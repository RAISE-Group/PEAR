def test_arith_series_with_array(self, data, all_arithmetic_operators):
    self._skip_if_different_combine(data)
    super().test_arith_series_with_array(data, all_arithmetic_operators)