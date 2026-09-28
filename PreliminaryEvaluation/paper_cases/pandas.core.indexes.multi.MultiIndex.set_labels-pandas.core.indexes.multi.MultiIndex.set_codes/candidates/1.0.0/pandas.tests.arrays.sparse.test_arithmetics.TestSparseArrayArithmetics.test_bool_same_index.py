@pytest.mark.parametrize('fill_value', [True, False, np.nan])
def test_bool_same_index(self, kind, fill_value):
    values = self._base([True, False, True, True], dtype=np.bool)
    rvalues = self._base([True, False, True, True], dtype=np.bool)
    a = self._klass(values, kind=kind, dtype=np.bool, fill_value=fill_value)
    b = self._klass(rvalues, kind=kind, dtype=np.bool, fill_value=fill_value)
    self._check_logical_ops(a, b, values, rvalues)