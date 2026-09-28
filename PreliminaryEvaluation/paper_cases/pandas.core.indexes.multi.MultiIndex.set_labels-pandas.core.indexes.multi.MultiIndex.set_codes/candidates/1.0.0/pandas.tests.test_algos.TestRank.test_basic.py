def test_basic(self):
    exp = np.array([1, 2], dtype=np.float64)
    for dtype in np.typecodes['AllInteger']:
        s = Series([1, 100], dtype=dtype)
        tm.assert_numpy_array_equal(algos.rank(s), exp)