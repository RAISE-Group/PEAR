def test_constructor_unsigned_dtype_overflow(self, uint_dtype):
    msg = 'Trying to coerce negative values to unsigned integers'
    with pytest.raises(OverflowError, match=msg):
        Series([-1], dtype=uint_dtype)