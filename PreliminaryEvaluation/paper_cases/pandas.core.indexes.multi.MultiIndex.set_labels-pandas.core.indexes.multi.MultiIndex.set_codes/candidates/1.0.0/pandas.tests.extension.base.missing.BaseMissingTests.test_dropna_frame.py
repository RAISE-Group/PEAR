def test_dropna_frame(self, data_missing):
    df = pd.DataFrame({'A': data_missing})
    result = df.dropna()
    expected = df.iloc[[1]]
    self.assert_frame_equal(result, expected)
    result = df.dropna(axis='columns')
    expected = pd.DataFrame(index=[0, 1])
    self.assert_frame_equal(result, expected)
    df = pd.DataFrame({'A': data_missing, 'B': [1, np.nan]})
    result = df.dropna()
    expected = df.iloc[:0]
    self.assert_frame_equal(result, expected)