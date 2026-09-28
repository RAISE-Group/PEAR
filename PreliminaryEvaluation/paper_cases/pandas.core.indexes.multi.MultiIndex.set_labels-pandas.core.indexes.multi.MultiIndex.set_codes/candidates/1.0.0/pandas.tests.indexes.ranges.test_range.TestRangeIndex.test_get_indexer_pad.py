def test_get_indexer_pad(self):
    index = self.create_index()
    target = RangeIndex(10)
    indexer = index.get_indexer(target, method='pad')
    expected = np.array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4], dtype=np.intp)
    tm.assert_numpy_array_equal(indexer, expected)