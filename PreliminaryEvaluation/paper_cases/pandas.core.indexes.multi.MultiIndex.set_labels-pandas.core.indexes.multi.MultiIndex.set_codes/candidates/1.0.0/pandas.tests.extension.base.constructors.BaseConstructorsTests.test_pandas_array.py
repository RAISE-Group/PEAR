def test_pandas_array(self, data):
    result = pd.array(data)
    self.assert_extension_array_equal(result, data)