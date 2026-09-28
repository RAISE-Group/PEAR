def test_get_indexer_nan(self):
    result = Index([1, 2, np.nan]).get_indexer([np.nan])
    expected = np.array([2], dtype=np.intp)
    tm.assert_numpy_array_equal(result, expected)