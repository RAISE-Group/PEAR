def test_is_lexsorted(self):
    levels = [[0, 1], [0, 1, 2]]
    index = MultiIndex(levels=levels, codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])
    assert index.is_lexsorted()
    index = MultiIndex(levels=levels, codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 2, 1]])
    assert not index.is_lexsorted()
    index = MultiIndex(levels=levels, codes=[[0, 0, 1, 0, 1, 1], [0, 1, 0, 2, 2, 1]])
    assert not index.is_lexsorted()
    assert index.lexsort_depth == 0