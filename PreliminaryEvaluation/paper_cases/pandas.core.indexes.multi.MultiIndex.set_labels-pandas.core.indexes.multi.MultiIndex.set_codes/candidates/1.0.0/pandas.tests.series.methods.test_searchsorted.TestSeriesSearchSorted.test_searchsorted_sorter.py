def test_searchsorted_sorter(self):
    ser = Series([3, 1, 2])
    res = ser.searchsorted([0, 3], sorter=np.argsort(ser))
    exp = np.array([0, 2], dtype=np.intp)
    tm.assert_numpy_array_equal(res, exp)