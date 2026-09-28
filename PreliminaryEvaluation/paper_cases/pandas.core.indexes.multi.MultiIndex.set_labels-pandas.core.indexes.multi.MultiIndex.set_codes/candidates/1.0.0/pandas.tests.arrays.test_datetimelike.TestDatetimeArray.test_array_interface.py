def test_array_interface(self, datetime_index):
    arr = DatetimeArray(datetime_index)
    result = np.asarray(arr)
    expected = arr._data
    assert result is expected
    tm.assert_numpy_array_equal(result, expected)
    result = np.array(arr, copy=False)
    assert result is expected
    tm.assert_numpy_array_equal(result, expected)
    result = np.asarray(arr, dtype='datetime64[ns]')
    expected = arr._data
    assert result is expected
    tm.assert_numpy_array_equal(result, expected)
    result = np.array(arr, dtype='datetime64[ns]', copy=False)
    assert result is expected
    tm.assert_numpy_array_equal(result, expected)
    result = np.array(arr, dtype='datetime64[ns]')
    assert result is not expected
    tm.assert_numpy_array_equal(result, expected)
    result = np.asarray(arr, dtype=object)
    expected = np.array(list(arr), dtype=object)
    tm.assert_numpy_array_equal(result, expected)
    result = np.asarray(arr, dtype='int64')
    assert result is not arr.asi8
    assert not np.may_share_memory(arr, result)
    expected = arr.asi8.copy()
    tm.assert_numpy_array_equal(result, expected)
    for dtype in ['float64', str]:
        result = np.asarray(arr, dtype=dtype)
        expected = np.asarray(arr).astype(dtype)
        tm.assert_numpy_array_equal(result, expected)