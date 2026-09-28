def test_is_numeric_array(self):
    assert lib.is_float_array(np.array([1, 2.0]))
    assert lib.is_float_array(np.array([1, 2.0, np.nan]))
    assert not lib.is_float_array(np.array([1, 2]))
    assert lib.is_integer_array(np.array([1, 2]))
    assert not lib.is_integer_array(np.array([1, 2.0]))