@pytest.mark.parametrize('constructor, expected_type, assert_func', [(IntervalIndex, np.array, tm.assert_numpy_array_equal), (Series, Series, tm.assert_series_equal)])
def test_index_series_compat(self, op, constructor, expected_type, assert_func):
    breaks = range(4)
    index = constructor(IntervalIndex.from_breaks(breaks))
    other = index[0]
    result = op(index, other)
    expected = expected_type(self.elementwise_comparison(op, index, other))
    assert_func(result, expected)
    other = breaks[0]
    result = op(index, other)
    expected = expected_type(self.elementwise_comparison(op, index, other))
    assert_func(result, expected)
    other = IntervalArray.from_breaks(breaks)
    result = op(index, other)
    expected = expected_type(self.elementwise_comparison(op, index, other))
    assert_func(result, expected)
    other = [index[0], breaks[0], 'foo']
    result = op(index, other)
    expected = expected_type(self.elementwise_comparison(op, index, other))
    assert_func(result, expected)