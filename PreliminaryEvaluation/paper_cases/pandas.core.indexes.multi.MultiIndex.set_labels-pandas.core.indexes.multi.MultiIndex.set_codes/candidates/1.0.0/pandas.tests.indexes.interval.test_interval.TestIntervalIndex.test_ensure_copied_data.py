def test_ensure_copied_data(self, closed):
    index = self.create_index(closed=closed)
    result = IntervalIndex(index, copy=False)
    tm.assert_numpy_array_equal(index.left.values, result.left.values, check_same='same')
    tm.assert_numpy_array_equal(index.right.values, result.right.values, check_same='same')
    result = IntervalIndex(index._ndarray_values, copy=False)
    tm.assert_numpy_array_equal(index.left.values, result.left.values, check_same='copy')
    tm.assert_numpy_array_equal(index.right.values, result.right.values, check_same='copy')