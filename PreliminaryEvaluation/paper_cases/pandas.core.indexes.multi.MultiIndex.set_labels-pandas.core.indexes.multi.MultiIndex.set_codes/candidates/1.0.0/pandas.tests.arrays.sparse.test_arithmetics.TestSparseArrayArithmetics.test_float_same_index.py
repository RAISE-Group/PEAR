def test_float_same_index(self, kind, mix, all_arithmetic_functions):
    op = all_arithmetic_functions
    values = self._base([np.nan, 1, 2, 0, np.nan, 0, 1, 2, 1, np.nan])
    rvalues = self._base([np.nan, 2, 3, 4, np.nan, 0, 1, 3, 2, np.nan])
    a = self._klass(values, kind=kind)
    b = self._klass(rvalues, kind=kind)
    self._check_numeric_ops(a, b, values, rvalues, mix, op)
    values = self._base([0.0, 1.0, 2.0, 6.0, 0.0, 0.0, 1.0, 2.0, 1.0, 0.0])
    rvalues = self._base([0.0, 2.0, 3.0, 4.0, 0.0, 0.0, 1.0, 3.0, 2.0, 0.0])
    a = self._klass(values, kind=kind, fill_value=0)
    b = self._klass(rvalues, kind=kind, fill_value=0)
    self._check_numeric_ops(a, b, values, rvalues, mix, op)