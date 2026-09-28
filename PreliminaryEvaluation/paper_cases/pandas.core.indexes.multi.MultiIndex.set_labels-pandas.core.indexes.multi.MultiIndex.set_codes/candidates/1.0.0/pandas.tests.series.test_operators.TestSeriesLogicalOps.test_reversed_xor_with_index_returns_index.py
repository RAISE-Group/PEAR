def test_reversed_xor_with_index_returns_index(self):
    ser = Series([True, True, False, False])
    idx1 = Index([True, False, True, False])
    idx2 = Index([1, 0, 1, 0])
    expected = Index.symmetric_difference(idx1, ser)
    result = idx1 ^ ser
    tm.assert_index_equal(result, expected)
    expected = Index.symmetric_difference(idx2, ser)
    result = idx2 ^ ser
    tm.assert_index_equal(result, expected)