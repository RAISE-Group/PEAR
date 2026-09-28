def test_array_interface(self, period_index):
    arr = PeriodArray(period_index)
    result = np.asarray(arr)
    expected = np.array(list(arr), dtype=object)
    tm.assert_numpy_array_equal(result, expected)
    result = np.asarray(arr, dtype=object)
    tm.assert_numpy_array_equal(result, expected)
    with pytest.raises(TypeError):
        np.asarray(arr, dtype='int64')
    with pytest.raises(TypeError):
        np.asarray(arr, dtype='float64')
    result = np.asarray(arr, dtype='S20')
    expected = np.asarray(arr).astype('S20')
    tm.assert_numpy_array_equal(result, expected)