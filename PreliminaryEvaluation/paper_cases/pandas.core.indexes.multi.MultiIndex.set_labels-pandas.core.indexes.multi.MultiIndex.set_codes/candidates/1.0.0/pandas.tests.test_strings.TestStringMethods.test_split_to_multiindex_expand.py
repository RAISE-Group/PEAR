def test_split_to_multiindex_expand(self):
    idx = Index(['nosplit', 'alsonosplit', np.nan])
    result = idx.str.split('_', expand=True)
    exp = idx
    tm.assert_index_equal(result, exp)
    assert result.nlevels == 1
    idx = Index(['some_equal_splits', 'with_no_nans', np.nan, None])
    result = idx.str.split('_', expand=True)
    exp = MultiIndex.from_tuples([('some', 'equal', 'splits'), ('with', 'no', 'nans'), [np.nan, np.nan, np.nan], [None, None, None]])
    tm.assert_index_equal(result, exp)
    assert result.nlevels == 3
    idx = Index(['some_unequal_splits', 'one_of_these_things_is_not', np.nan, None])
    result = idx.str.split('_', expand=True)
    exp = MultiIndex.from_tuples([('some', 'unequal', 'splits', np.nan, np.nan, np.nan), ('one', 'of', 'these', 'things', 'is', 'not'), (np.nan, np.nan, np.nan, np.nan, np.nan, np.nan), (None, None, None, None, None, None)])
    tm.assert_index_equal(result, exp)
    assert result.nlevels == 6
    with pytest.raises(ValueError, match='expand must be'):
        idx.str.split('_', expand='not_a_boolean')