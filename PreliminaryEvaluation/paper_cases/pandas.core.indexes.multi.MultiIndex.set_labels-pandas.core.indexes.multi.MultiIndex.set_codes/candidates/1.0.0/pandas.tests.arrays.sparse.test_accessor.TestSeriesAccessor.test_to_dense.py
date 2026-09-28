def test_to_dense(self):
    s = pd.Series([0, 1, 0, 10], dtype='Sparse[int64]')
    result = s.sparse.to_dense()
    expected = pd.Series([0, 1, 0, 10])
    tm.assert_series_equal(result, expected)