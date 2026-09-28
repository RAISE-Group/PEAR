def test_bounds_check_small(self):
    arr = np.array([1, 2, 3], dtype=np.int64)
    indexer = [0, -1, -2]
    with pytest.raises(ValueError):
        algos.take(arr, indexer, allow_fill=True)
    result = algos.take(arr, indexer)
    expected = np.array([1, 3, 2], dtype=np.int64)
    tm.assert_numpy_array_equal(result, expected)