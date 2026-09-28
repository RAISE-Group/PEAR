def test_rsplit_to_multiindex_expand(self):
    idx = Index(['nosplit', 'alsonosplit'])
    result = idx.str.rsplit('_', expand=True)
    exp = idx
    tm.assert_index_equal(result, exp)
    assert result.nlevels == 1
    idx = Index(['some_equal_splits', 'with_no_nans'])
    result = idx.str.rsplit('_', expand=True)
    exp = MultiIndex.from_tuples([('some', 'equal', 'splits'), ('with', 'no', 'nans')])
    tm.assert_index_equal(result, exp)
    assert result.nlevels == 3
    idx = Index(['some_equal_splits', 'with_no_nans'])
    result = idx.str.rsplit('_', expand=True, n=1)
    exp = MultiIndex.from_tuples([('some_equal', 'splits'), ('with_no', 'nans')])
    tm.assert_index_equal(result, exp)
    assert result.nlevels == 2