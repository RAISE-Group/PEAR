def test_take_na_empty(self):
    result = algos.take(np.array([]), [-1, -1], allow_fill=True, fill_value=0.0)
    expected = np.array([0.0, 0.0])
    tm.assert_numpy_array_equal(result, expected)