def test_reindexing(self):
    np.random.seed(123456789)
    ci = self.create_index()
    oidx = Index(np.array(ci))
    for n in [1, 2, 5, len(ci)]:
        finder = oidx[np.random.randint(0, len(ci), size=n)]
        expected = oidx.get_indexer_non_unique(finder)[0]
        actual = ci.get_indexer(finder)
        tm.assert_numpy_array_equal(expected, actual)
    for finder in [list('aabbca'), list('aababca')]:
        expected = oidx.get_indexer_non_unique(finder)[0]
        actual = ci.get_indexer(finder)
        tm.assert_numpy_array_equal(expected, actual)