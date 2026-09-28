def test_argsort(self, data_for_sorting):
    result = pd.Series(data_for_sorting).argsort()
    expected = pd.Series(np.array([2, 0, 1], dtype=np.int64))
    self.assert_series_equal(result, expected)