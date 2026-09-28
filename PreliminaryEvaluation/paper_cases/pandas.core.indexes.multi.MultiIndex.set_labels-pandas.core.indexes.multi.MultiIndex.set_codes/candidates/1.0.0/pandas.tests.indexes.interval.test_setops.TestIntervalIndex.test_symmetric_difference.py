def test_symmetric_difference(self, closed, sort):
    index = monotonic_index(0, 11, closed=closed)
    result = index[1:].symmetric_difference(index[:-1], sort=sort)
    expected = IntervalIndex([index[0], index[-1]])
    if sort is None:
        tm.assert_index_equal(result, expected)
    assert tm.equalContents(result, expected)
    result = index.symmetric_difference(index, sort=sort)
    expected = empty_index(dtype='int64', closed=closed)
    if sort is None:
        tm.assert_index_equal(result, expected)
    assert tm.equalContents(result, expected)
    other = IntervalIndex.from_arrays(index.left.astype('float64'), index.right, closed=closed)
    result = index.symmetric_difference(other, sort=sort)
    tm.assert_index_equal(result, expected)