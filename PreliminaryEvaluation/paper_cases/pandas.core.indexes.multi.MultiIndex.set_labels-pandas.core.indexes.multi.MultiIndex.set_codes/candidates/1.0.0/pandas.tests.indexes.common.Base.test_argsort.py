def test_argsort(self, request, indices):
    if isinstance(indices, CategoricalIndex):
        return
    result = indices.argsort()
    expected = np.array(indices).argsort()
    tm.assert_numpy_array_equal(result, expected, check_dtype=False)