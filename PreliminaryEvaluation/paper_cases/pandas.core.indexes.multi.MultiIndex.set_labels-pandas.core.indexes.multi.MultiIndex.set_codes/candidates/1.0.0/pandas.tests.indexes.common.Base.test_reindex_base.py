def test_reindex_base(self):
    idx = self.create_index()
    expected = np.arange(idx.size, dtype=np.intp)
    actual = idx.get_indexer(idx)
    tm.assert_numpy_array_equal(expected, actual)
    with pytest.raises(ValueError, match='Invalid fill method'):
        idx.get_indexer(idx, method='invalid')