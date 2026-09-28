def test_astype_str(self, data):
    result = pd.Series(data[:5]).astype(str)
    expected = pd.Series(data[:5].astype(str))
    self.assert_series_equal(result, expected)