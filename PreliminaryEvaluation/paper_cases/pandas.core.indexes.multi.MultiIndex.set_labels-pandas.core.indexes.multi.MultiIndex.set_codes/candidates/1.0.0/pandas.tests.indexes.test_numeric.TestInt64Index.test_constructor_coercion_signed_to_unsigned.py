def test_constructor_coercion_signed_to_unsigned(self, uint_dtype):
    msg = 'Trying to coerce negative values to unsigned integers'
    with pytest.raises(OverflowError, match=msg):
        Index([-1], dtype=uint_dtype)