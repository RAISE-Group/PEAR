def test_fillna_scalar(self, data_missing):
    valid = data_missing[1]
    result = data_missing.fillna(valid)
    expected = data_missing.fillna(valid)
    self.assert_extension_array_equal(result, expected)