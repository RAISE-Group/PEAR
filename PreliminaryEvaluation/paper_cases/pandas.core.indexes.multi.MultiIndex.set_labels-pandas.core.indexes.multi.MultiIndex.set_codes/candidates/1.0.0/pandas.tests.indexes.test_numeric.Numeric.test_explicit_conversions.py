def test_explicit_conversions(self):
    idx = self._holder(np.arange(5, dtype='int64'))
    arr = np.arange(5, dtype='int64') * 3.2
    expected = Float64Index(arr)
    fidx = idx * 3.2
    tm.assert_index_equal(fidx, expected)
    fidx = 3.2 * idx
    tm.assert_index_equal(fidx, expected)
    expected = Float64Index(arr)
    a = np.zeros(5, dtype='float64')
    result = fidx - a
    tm.assert_index_equal(result, expected)
    expected = Float64Index(-arr)
    a = np.zeros(5, dtype='float64')
    result = a - fidx
    tm.assert_index_equal(result, expected)