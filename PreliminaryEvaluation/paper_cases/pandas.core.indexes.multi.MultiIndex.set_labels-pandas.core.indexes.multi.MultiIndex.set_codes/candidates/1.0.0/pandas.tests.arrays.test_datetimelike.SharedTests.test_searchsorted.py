def test_searchsorted(self):
    data = np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9
    arr = self.array_cls(data, freq='D')
    result = arr.searchsorted(arr[1])
    assert result == 1
    result = arr.searchsorted(arr[2], side='right')
    assert result == 3
    result = arr.searchsorted(arr[1:3])
    expected = np.array([1, 2], dtype=np.intp)
    tm.assert_numpy_array_equal(result, expected)
    result = arr.searchsorted(arr[1:3], side='right')
    expected = np.array([2, 3], dtype=np.intp)
    tm.assert_numpy_array_equal(result, expected)
    result = arr.searchsorted(pd.NaT)
    assert result == 0