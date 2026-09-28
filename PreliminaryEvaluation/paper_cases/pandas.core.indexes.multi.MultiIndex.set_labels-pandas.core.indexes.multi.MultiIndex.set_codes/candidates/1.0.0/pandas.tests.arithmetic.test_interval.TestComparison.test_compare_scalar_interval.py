def test_compare_scalar_interval(self, op, array):
    other = array[0]
    result = op(array, other)
    expected = self.elementwise_comparison(op, array, other)
    tm.assert_numpy_array_equal(result, expected)
    other = Interval(array.left[0], array.right[1])
    result = op(array, other)
    expected = self.elementwise_comparison(op, array, other)
    tm.assert_numpy_array_equal(result, expected)