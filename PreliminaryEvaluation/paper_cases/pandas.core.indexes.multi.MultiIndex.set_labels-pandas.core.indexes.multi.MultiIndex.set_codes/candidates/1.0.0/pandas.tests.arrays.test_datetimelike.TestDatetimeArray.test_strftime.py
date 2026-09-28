def test_strftime(self, datetime_index):
    arr = DatetimeArray(datetime_index)
    result = arr.strftime('%Y %b')
    expected = np.array([ts.strftime('%Y %b') for ts in arr], dtype=object)
    tm.assert_numpy_array_equal(result, expected)