def test_append(self, closed):
    index1 = IntervalIndex.from_arrays([0, 1], [1, 2], closed=closed)
    index2 = IntervalIndex.from_arrays([1, 2], [2, 3], closed=closed)
    result = index1.append(index2)
    expected = IntervalIndex.from_arrays([0, 1, 1, 2], [1, 2, 2, 3], closed=closed)
    tm.assert_index_equal(result, expected)
    result = index1.append([index1, index2])
    expected = IntervalIndex.from_arrays([0, 1, 0, 1, 1, 2], [1, 2, 1, 2, 2, 3], closed=closed)
    tm.assert_index_equal(result, expected)
    msg = 'can only append two IntervalIndex objects that are closed on the same side'
    for other_closed in {'left', 'right', 'both', 'neither'} - {closed}:
        index_other_closed = IntervalIndex.from_arrays([0, 1], [1, 2], closed=other_closed)
        with pytest.raises(ValueError, match=msg):
            index1.append(index_other_closed)