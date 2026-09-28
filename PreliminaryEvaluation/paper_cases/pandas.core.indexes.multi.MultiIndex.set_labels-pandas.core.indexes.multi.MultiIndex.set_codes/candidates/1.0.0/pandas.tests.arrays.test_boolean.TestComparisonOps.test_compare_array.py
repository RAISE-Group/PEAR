def test_compare_array(self, data, all_compare_operators):
    op_name = all_compare_operators
    other = pd.array([True] * len(data), dtype='boolean')
    self._compare_other(data, op_name, other)
    other = np.array([True] * len(data))
    self._compare_other(data, op_name, other)
    other = pd.Series([True] * len(data))
    self._compare_other(data, op_name, other)