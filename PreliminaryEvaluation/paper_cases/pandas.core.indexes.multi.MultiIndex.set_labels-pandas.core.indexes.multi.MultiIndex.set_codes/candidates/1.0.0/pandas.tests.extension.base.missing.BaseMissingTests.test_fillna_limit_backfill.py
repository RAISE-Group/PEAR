def test_fillna_limit_backfill(self, data_missing):
    arr = data_missing.take([1, 0, 0, 0, 1])
    result = pd.Series(arr).fillna(method='backfill', limit=2)
    expected = pd.Series(data_missing.take([1, 0, 1, 1, 1]))
    self.assert_series_equal(result, expected)