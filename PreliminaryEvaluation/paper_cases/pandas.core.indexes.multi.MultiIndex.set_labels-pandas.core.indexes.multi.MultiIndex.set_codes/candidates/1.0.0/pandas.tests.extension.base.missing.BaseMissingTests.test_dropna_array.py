def test_dropna_array(self, data_missing):
    result = data_missing.dropna()
    expected = data_missing[[1]]
    self.assert_extension_array_equal(result, expected)