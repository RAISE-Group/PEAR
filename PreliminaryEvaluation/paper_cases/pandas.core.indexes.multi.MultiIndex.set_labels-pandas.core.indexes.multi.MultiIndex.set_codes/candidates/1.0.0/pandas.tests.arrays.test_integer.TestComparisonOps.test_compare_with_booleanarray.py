def test_compare_with_booleanarray(self, all_compare_operators):
    op = self.get_op_from_name(all_compare_operators)
    a = pd.array([True, False, None] * 3, dtype='boolean')
    b = pd.array([0] * 3 + [1] * 3 + [None] * 3, dtype='Int64')
    other = pd.array([False] * 3 + [True] * 3 + [None] * 3, dtype='boolean')
    expected = op(a, other)
    result = op(a, b)
    tm.assert_extension_array_equal(result, expected)