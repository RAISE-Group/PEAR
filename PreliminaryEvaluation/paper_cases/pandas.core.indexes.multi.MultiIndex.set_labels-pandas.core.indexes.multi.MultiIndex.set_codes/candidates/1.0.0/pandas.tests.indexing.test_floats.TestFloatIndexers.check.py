def check(self, result, original, indexer, getitem):
    """
        comparator for results
        we need to take care if we are indexing on a
        Series or a frame
        """
    if isinstance(original, Series):
        expected = original.iloc[indexer]
    elif getitem:
        expected = original.iloc[:, indexer]
    else:
        expected = original.iloc[indexer]
    tm.assert_almost_equal(result, expected)