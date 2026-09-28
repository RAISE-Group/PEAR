def test_get_indexer_nearest_error(self):
    index = Index(np.arange(10))
    with pytest.raises(ValueError, match='limit argument'):
        index.get_indexer([1, 0], method='nearest', limit=1)
    with pytest.raises(ValueError, match='tolerance size must match'):
        index.get_indexer([1, 0], method='nearest', tolerance=[1, 2, 3])