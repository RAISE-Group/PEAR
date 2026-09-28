def test_indexing_over_hashtable_size_cutoff(self):
    n = 10000
    old_cutoff = _index._SIZE_CUTOFF
    _index._SIZE_CUTOFF = 20000
    s = Series(np.arange(n), MultiIndex.from_arrays((['a'] * n, np.arange(n))))
    assert s['a', 5] == 5
    assert s['a', 6] == 6
    assert s['a', 7] == 7
    _index._SIZE_CUTOFF = old_cutoff