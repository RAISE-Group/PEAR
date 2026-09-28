def test_compare_list_like_nan(self, op, array, nulls_fixture):
    other = [nulls_fixture] * 4
    result = op(array, other)
    expected = self.elementwise_comparison(op, array, other)
    tm.assert_numpy_array_equal(result, expected)