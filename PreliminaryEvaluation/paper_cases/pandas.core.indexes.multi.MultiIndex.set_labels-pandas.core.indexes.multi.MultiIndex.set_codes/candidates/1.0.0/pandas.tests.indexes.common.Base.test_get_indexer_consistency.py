def test_get_indexer_consistency(self, indices):
    if isinstance(indices, IntervalIndex):
        return
    if indices.is_unique or isinstance(indices, CategoricalIndex):
        indexer = indices.get_indexer(indices[0:2])
        assert isinstance(indexer, np.ndarray)
        assert indexer.dtype == np.intp
    else:
        e = 'Reindexing only valid with uniquely valued Index objects'
        with pytest.raises(InvalidIndexError, match=e):
            indices.get_indexer(indices[0:2])
    indexer, _ = indices.get_indexer_non_unique(indices[0:2])
    assert isinstance(indexer, np.ndarray)
    assert indexer.dtype == np.intp