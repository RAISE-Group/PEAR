def test_get_indexer_backfill(self):
    index = self.create_index()
    target = RangeIndex(10)
    indexer = index.get_indexer(target, method='backfill')
    expected = np.array([0, 1, 1, 2, 2, 3, 3, 4, 4, 5], dtype=np.intp)
    tm.assert_numpy_array_equal(indexer, expected)