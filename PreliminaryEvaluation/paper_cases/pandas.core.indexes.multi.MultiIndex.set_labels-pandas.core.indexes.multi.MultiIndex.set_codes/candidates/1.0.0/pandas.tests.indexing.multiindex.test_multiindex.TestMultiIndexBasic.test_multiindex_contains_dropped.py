def test_multiindex_contains_dropped(self):
    idx = MultiIndex.from_product([[1, 2], [3, 4]])
    assert 2 in idx
    idx = idx.drop(2)
    assert 2 in idx.levels[0]
    assert 2 not in idx
    idx = MultiIndex.from_product([['a', 'b'], ['c', 'd']])
    assert 'a' in idx
    idx = idx.drop('a')
    assert 'a' in idx.levels[0]
    assert 'a' not in idx