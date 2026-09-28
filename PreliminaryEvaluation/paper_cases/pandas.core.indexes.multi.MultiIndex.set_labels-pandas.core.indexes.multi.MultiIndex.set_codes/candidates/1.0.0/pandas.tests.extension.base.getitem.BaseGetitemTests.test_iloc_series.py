def test_iloc_series(self, data):
    ser = pd.Series(data)
    result = ser.iloc[:4]
    expected = pd.Series(data[:4])
    self.assert_series_equal(result, expected)
    result = ser.iloc[[0, 1, 2, 3]]
    self.assert_series_equal(result, expected)