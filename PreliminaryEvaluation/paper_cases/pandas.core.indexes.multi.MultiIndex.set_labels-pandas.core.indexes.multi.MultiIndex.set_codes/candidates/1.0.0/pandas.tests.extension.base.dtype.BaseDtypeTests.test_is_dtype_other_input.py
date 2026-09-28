def test_is_dtype_other_input(self, dtype):
    assert dtype.is_dtype([1, 2, 3]) is False