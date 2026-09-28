def test_array(self, all_compare_operators):
    op = self.get_op_from_name(all_compare_operators)
    a = pd.array([True] * 3 + [False] * 3 + [None] * 3, dtype='boolean')
    b = pd.array([True, False, None] * 3, dtype='boolean')
    result = op(a, b)
    values = op(a._data, b._data)
    mask = a._mask | b._mask
    expected = BooleanArray(values, mask)
    tm.assert_extension_array_equal(result, expected)
    result[0] = None
    tm.assert_extension_array_equal(a, pd.array([True] * 3 + [False] * 3 + [None] * 3, dtype='boolean'))
    tm.assert_extension_array_equal(b, pd.array([True, False, None] * 3, dtype='boolean'))