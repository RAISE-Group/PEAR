def test_count(self, data_missing):
    df = pd.DataFrame({'A': data_missing})
    result = df.count(axis='columns')
    expected = pd.Series([0, 1])
    self.assert_series_equal(result, expected)