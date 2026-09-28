def test_unstack_non_unique_index_names(self):
    idx = MultiIndex.from_tuples([('a', 'b'), ('c', 'd')], names=['c1', 'c1'])
    df = DataFrame([1, 2], index=idx)
    with pytest.raises(ValueError):
        df.unstack('c1')
    with pytest.raises(ValueError):
        df.T.stack('c1')