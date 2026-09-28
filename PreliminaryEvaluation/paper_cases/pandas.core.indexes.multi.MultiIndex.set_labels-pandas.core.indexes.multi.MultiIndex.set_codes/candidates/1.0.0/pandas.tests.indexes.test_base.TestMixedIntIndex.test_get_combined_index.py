def test_get_combined_index(self):
    result = _get_combined_index([])
    expected = Index([])
    tm.assert_index_equal(result, expected)