def test_get_indexer(self):
    idx1 = CategoricalIndex(list('aabcde'), categories=list('edabc'))
    idx2 = CategoricalIndex(list('abf'))
    for indexer in [idx2, list('abf'), Index(list('abf'))]:
        r1 = idx1.get_indexer(idx2)
        tm.assert_almost_equal(r1, np.array([0, 1, 2, -1], dtype=np.intp))
    msg = "method='pad' and method='backfill' not implemented yet for CategoricalIndex"
    with pytest.raises(NotImplementedError, match=msg):
        idx2.get_indexer(idx1, method='pad')
    with pytest.raises(NotImplementedError, match=msg):
        idx2.get_indexer(idx1, method='backfill')
    msg = "method='nearest' not implemented yet for CategoricalIndex"
    with pytest.raises(NotImplementedError, match=msg):
        idx2.get_indexer(idx1, method='nearest')