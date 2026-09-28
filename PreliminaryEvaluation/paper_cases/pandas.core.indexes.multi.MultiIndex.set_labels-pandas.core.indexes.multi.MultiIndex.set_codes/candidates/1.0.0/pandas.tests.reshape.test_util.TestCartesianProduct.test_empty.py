def test_empty(self):
    X = [[], [0, 1], []]
    Y = [[], [], ['a', 'b', 'c']]
    for x, y in zip(X, Y):
        expected1 = np.array([], dtype=np.asarray(x).dtype)
        expected2 = np.array([], dtype=np.asarray(y).dtype)
        result1, result2 = cartesian_product([x, y])
        tm.assert_numpy_array_equal(result1, expected1)
        tm.assert_numpy_array_equal(result2, expected2)
    result = cartesian_product([])
    expected = []
    assert result == expected