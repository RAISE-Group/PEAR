def test_searchsorted_numeric_dtypes_vector(self, any_real_dtype):
    arr = pd.array([1, 3, 90], dtype=any_real_dtype)
    result = arr.searchsorted([2, 30])
    expected = np.array([1, 2], dtype=np.intp)
    tm.assert_numpy_array_equal(result, expected)