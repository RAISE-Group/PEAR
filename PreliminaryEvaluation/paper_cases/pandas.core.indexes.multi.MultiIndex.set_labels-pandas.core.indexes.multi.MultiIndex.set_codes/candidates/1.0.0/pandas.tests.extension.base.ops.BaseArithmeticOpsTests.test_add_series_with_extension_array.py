def test_add_series_with_extension_array(self, data):
    s = pd.Series(data)
    result = s + data
    expected = pd.Series(data + data)
    self.assert_series_equal(result, expected)