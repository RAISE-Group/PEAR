def test_1d_bool(self):
    arr = np.array([0, 1, 0], dtype=bool)
    result = algos.take_1d(arr, [0, 2, 2, 1])
    expected = arr.take([0, 2, 2, 1])
    tm.assert_numpy_array_equal(result, expected)
    result = algos.take_1d(arr, [0, 2, -1])
    assert result.dtype == np.object_