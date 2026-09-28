def test_is_dtype_unboxes_dtype(self, data, dtype):
    assert dtype.is_dtype(data) is True