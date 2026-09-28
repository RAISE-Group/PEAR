def test_pow_array(self):
    a = integer_array([0, 0, 0, 1, 1, 1, None, None, None])
    b = integer_array([0, 1, None, 0, 1, None, 0, 1, None])
    result = a ** b
    expected = integer_array([1, 0, None, 1, 1, 1, 1, None, None])
    tm.assert_extension_array_equal(result, expected)