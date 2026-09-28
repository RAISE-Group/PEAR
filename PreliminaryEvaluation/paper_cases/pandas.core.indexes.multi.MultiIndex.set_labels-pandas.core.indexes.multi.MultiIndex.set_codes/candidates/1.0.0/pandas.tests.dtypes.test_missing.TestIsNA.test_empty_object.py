def test_empty_object(self):
    for shape in [(4, 0), (4,)]:
        arr = np.empty(shape=shape, dtype=object)
        result = isna(arr)
        expected = np.ones(shape=shape, dtype=bool)
        tm.assert_numpy_array_equal(result, expected)