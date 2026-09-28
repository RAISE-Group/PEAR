def test_take_coerces_list(self):
    arr = [1, 2, 3]
    result = algos.take(arr, [0, 0])
    expected = np.array([1, 1])
    tm.assert_numpy_array_equal(result, expected)