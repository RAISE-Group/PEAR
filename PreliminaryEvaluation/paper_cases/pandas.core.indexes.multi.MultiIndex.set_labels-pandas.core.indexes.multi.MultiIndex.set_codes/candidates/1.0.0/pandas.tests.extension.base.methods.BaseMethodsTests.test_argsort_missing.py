def test_argsort_missing(self, data_missing_for_sorting):
    result = pd.Series(data_missing_for_sorting).argsort()
    expected = pd.Series(np.array([1, -1, 0], dtype=np.int64))
    self.assert_series_equal(result, expected)