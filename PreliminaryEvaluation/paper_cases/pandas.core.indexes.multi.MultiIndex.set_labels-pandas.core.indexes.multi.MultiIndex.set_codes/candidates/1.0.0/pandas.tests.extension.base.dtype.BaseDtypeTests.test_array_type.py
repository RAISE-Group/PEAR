def test_array_type(self, data, dtype):
    assert dtype.construct_array_type() is type(data)