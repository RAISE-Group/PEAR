def test_to_numpy(self, data):
    expected = np.asarray(data)
    result = data.to_numpy()
    self.assert_equal(result, expected)
    result = pd.Series(data).to_numpy()
    self.assert_equal(result, expected)