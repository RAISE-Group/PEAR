def test_uint64_overflow(self):
    exp = np.array([1, 2], dtype=np.float64)
    for dtype in [np.float64, np.uint64]:
        s = Series([1, 2 ** 63], dtype=dtype)
        tm.assert_numpy_array_equal(algos.rank(s), exp)