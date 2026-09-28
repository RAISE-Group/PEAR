def test_compare_scalar_interval_mixed_closed(self, op, closed, other_closed):
    array = IntervalArray.from_arrays(range(2), range(1, 3), closed=closed)
    other = Interval(0, 1, closed=other_closed)
    result = op(array, other)
    expected = self.elementwise_comparison(op, array, other)
    tm.assert_numpy_array_equal(result, expected)