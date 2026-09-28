def test_construct_from_string(self, dtype):
    dtype_instance = type(dtype).construct_from_string(dtype.name)
    assert isinstance(dtype_instance, type(dtype))