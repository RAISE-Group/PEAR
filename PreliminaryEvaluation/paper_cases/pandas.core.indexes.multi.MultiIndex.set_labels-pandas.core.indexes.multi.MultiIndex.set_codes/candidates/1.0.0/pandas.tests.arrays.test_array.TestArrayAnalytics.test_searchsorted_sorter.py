def test_searchsorted_sorter(self, any_real_dtype):
    arr = pd.array([3, 1, 2], dtype=any_real_dtype)
    result = arr.searchsorted([0, 3], sorter=np.argsort(arr))
    expected = np.array([0, 2], dtype=np.intp)
    tm.assert_numpy_array_equal(result, expected)