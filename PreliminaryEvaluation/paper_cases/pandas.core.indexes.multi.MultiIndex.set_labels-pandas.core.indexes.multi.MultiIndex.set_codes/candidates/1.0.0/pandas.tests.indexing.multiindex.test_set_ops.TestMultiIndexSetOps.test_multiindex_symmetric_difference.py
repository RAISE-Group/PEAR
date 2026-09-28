def test_multiindex_symmetric_difference(self):
    idx = MultiIndex.from_product([['a', 'b'], ['A', 'B']], names=['a', 'b'])
    result = idx ^ idx
    assert result.names == idx.names
    idx2 = idx.copy().rename(['A', 'B'])
    result = idx ^ idx2
    assert result.names == [None, None]