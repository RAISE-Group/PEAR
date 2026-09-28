def test_from_sequence_from_cls(self, data):
    result = type(data)._from_sequence(data, dtype=data.dtype)
    self.assert_extension_array_equal(result, data)
    data = data[:0]
    result = type(data)._from_sequence(data, dtype=data.dtype)
    self.assert_extension_array_equal(result, data)