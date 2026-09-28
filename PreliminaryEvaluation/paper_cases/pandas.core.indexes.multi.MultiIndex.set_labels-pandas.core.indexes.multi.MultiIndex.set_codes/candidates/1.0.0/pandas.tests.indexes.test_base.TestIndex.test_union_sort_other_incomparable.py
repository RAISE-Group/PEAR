def test_union_sort_other_incomparable(self):
    idx = pd.Index([1, pd.Timestamp('2000')])
    with tm.assert_produces_warning(RuntimeWarning):
        result = idx.union(idx[:1])
    tm.assert_index_equal(result, idx)
    with tm.assert_produces_warning(RuntimeWarning):
        result = idx.union(idx[:1], sort=None)
    tm.assert_index_equal(result, idx)
    result = idx.union(idx[:1], sort=False)
    tm.assert_index_equal(result, idx)