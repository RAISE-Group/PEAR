def test_constructor(self):
    index = Int64Index([-5, 0, 1, 2])
    expected = Index([-5, 0, 1, 2], dtype=np.int64)
    tm.assert_index_equal(index, expected)
    index = Int64Index(iter([-5, 0, 1, 2]))
    tm.assert_index_equal(index, expected)
    msg = 'Int64Index\\(\\.\\.\\.\\) must be called with a collection of some kind, 5 was passed'
    with pytest.raises(TypeError, match=msg):
        Int64Index(5)
    arr = index.values
    new_index = Int64Index(arr, copy=True)
    tm.assert_index_equal(new_index, index)
    val = arr[0] + 3000
    arr[0] = val
    assert new_index[0] != val
    expected = Int64Index([5, 0])
    for cls in [Index, Int64Index]:
        for idx in [cls([5, 0], dtype='int64'), cls(np.array([5, 0]), dtype='int64'), cls(Series([5, 0]), dtype='int64')]:
            tm.assert_index_equal(idx, expected)