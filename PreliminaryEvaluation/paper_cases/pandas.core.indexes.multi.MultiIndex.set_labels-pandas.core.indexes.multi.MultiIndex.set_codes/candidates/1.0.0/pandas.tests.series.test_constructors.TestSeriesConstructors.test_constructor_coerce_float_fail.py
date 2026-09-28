def test_constructor_coerce_float_fail(self, any_int_dtype):
    msg = 'Trying to coerce float values to integers'
    with pytest.raises(ValueError, match=msg):
        Series([1, 2, 3.5], dtype=any_int_dtype)