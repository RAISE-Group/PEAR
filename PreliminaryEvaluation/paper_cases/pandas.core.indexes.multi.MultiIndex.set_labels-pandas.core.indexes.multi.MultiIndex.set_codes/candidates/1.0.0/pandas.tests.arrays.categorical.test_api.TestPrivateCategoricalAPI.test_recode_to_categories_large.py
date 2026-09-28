def test_recode_to_categories_large(self):
    N = 1000
    codes = np.arange(N)
    old = Index(codes)
    expected = np.arange(N - 1, -1, -1, dtype=np.int16)
    new = Index(expected)
    result = _recode_for_categories(codes, old, new)
    tm.assert_numpy_array_equal(result, expected)