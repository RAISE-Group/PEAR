def test_is_dtype_from_name(self, dtype):
    result = type(dtype).is_dtype(dtype.name)
    assert result is True