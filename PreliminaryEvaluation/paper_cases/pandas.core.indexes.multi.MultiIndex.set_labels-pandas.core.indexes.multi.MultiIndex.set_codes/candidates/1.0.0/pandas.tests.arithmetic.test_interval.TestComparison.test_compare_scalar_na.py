def test_compare_scalar_na(self, op, array, nulls_fixture):
    result = op(array, nulls_fixture)
    expected = self.elementwise_comparison(op, array, nulls_fixture)
    tm.assert_numpy_array_equal(result, expected)