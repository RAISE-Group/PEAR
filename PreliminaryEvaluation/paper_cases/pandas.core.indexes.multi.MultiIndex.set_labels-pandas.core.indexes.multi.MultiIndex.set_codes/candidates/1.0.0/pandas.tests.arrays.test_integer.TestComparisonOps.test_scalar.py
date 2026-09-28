@pytest.mark.parametrize('other', [True, False, pd.NA, -1, 0, 1])
def test_scalar(self, other, all_compare_operators):
    op = self.get_op_from_name(all_compare_operators)
    a = pd.array([1, 0, None], dtype='Int64')
    result = op(a, other)
    if other is pd.NA:
        expected = pd.array([None, None, None], dtype='boolean')
    else:
        values = op(a._data, other)
        expected = pd.arrays.BooleanArray(values, a._mask, copy=True)
    tm.assert_extension_array_equal(result, expected)
    result[0] = pd.NA
    tm.assert_extension_array_equal(a, pd.array([1, 0, None], dtype='Int64'))