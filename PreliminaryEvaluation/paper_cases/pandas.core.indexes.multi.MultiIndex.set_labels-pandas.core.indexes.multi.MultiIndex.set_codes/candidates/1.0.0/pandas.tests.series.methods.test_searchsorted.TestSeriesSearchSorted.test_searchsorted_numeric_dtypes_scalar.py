def test_searchsorted_numeric_dtypes_scalar(self):
    ser = Series([1, 2, 90, 1000, 3000000000.0])
    res = ser.searchsorted(30)
    assert is_scalar(res)
    assert res == 2
    res = ser.searchsorted([30])
    exp = np.array([2], dtype=np.intp)
    tm.assert_numpy_array_equal(res, exp)