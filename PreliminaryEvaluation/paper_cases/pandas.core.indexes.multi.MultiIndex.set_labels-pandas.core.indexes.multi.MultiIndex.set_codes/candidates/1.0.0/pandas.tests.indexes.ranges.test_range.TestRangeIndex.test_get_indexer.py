def test_get_indexer(self):
    index = self.create_index()
    target = RangeIndex(10)
    indexer = index.get_indexer(target)
    expected = np.array([0, -1, 1, -1, 2, -1, 3, -1, 4, -1], dtype=np.intp)
    tm.assert_numpy_array_equal(indexer, expected)