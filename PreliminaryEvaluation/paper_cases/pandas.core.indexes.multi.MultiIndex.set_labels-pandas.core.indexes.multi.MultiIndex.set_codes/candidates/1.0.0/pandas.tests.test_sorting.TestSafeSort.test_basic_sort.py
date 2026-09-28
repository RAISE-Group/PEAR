def test_basic_sort(self):
    values = [3, 1, 2, 0, 4]
    result = safe_sort(values)
    expected = np.array([0, 1, 2, 3, 4])
    tm.assert_numpy_array_equal(result, expected)
    values = list('baaacb')
    result = safe_sort(values)
    expected = np.array(list('aaabbc'), dtype='object')
    tm.assert_numpy_array_equal(result, expected)
    values = []
    result = safe_sort(values)
    expected = np.array([])
    tm.assert_numpy_array_equal(result, expected)