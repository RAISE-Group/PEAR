def test_extension_array(self):
    a = array([1, 3, 2], dtype='Int64')
    result = safe_sort(a)
    expected = array([1, 2, 3], dtype='Int64')
    tm.assert_extension_array_equal(result, expected)