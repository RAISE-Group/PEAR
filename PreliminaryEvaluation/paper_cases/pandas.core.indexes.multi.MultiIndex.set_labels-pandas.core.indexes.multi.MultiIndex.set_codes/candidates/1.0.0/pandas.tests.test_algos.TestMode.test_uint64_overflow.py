def test_uint64_overflow(self):
    exp = Series([2 ** 63], dtype=np.uint64)
    s = Series([1, 2 ** 63, 2 ** 63], dtype=np.uint64)
    tm.assert_series_equal(algos.mode(s), exp)
    exp = Series([1, 2 ** 63], dtype=np.uint64)
    s = Series([1, 2 ** 63], dtype=np.uint64)
    tm.assert_series_equal(algos.mode(s), exp)