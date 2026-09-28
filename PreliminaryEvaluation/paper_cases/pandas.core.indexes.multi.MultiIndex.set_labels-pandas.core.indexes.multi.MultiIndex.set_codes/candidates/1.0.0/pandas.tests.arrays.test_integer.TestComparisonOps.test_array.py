def test_array(self, all_compare_operators):
    op = self.get_op_from_name(all_compare_operators)
    a = pd.array([0, 1, 2, None, None, None], dtype='Int64')
    b = pd.array([0, 1, None, 0, 1, None], dtype='Int64')
    result = op(a, b)
    values = op(a._data, b._data)
    mask = a._mask | b._mask
    expected = pd.arrays.BooleanArray(values, mask)
    tm.assert_extension_array_equal(result, expected)
    result[0] = pd.NA
    tm.assert_extension_array_equal(a, pd.array([0, 1, 2, None, None, None], dtype='Int64'))
    tm.assert_extension_array_equal(b, pd.array([0, 1, None, 0, 1, None], dtype='Int64'))