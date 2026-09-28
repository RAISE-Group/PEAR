def test_is_dtype_from_self(self, dtype):
    result = type(dtype).is_dtype(dtype)
    assert result is True