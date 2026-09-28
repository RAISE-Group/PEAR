def test_searchsorted_numeric_dtypes_vector(self):
    ser = Series([1, 2, 90, 1000, 3000000000.0])
    res = ser.searchsorted([91, 2000000.0])
    exp = np.array([3, 4], dtype=np.intp)
    tm.assert_numpy_array_equal(res, exp)