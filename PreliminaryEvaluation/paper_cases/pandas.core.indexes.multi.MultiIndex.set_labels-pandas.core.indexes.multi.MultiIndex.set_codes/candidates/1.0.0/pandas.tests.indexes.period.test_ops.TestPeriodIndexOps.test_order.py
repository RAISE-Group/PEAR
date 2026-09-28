def test_order(self):
    for freq in ['D', '2D', '4D']:
        idx = PeriodIndex(['2011-01-01', '2011-01-02', '2011-01-03'], freq=freq, name='idx')
        ordered = idx.sort_values()
        tm.assert_index_equal(ordered, idx)
        assert ordered.freq == idx.freq
        ordered = idx.sort_values(ascending=False)
        expected = idx[::-1]
        tm.assert_index_equal(ordered, expected)
        assert ordered.freq == expected.freq
        assert ordered.freq == freq
        ordered, indexer = idx.sort_values(return_indexer=True)
        tm.assert_index_equal(ordered, idx)
        tm.assert_numpy_array_equal(indexer, np.array([0, 1, 2]), check_dtype=False)
        assert ordered.freq == idx.freq
        assert ordered.freq == freq
        ordered, indexer = idx.sort_values(return_indexer=True, ascending=False)
        expected = idx[::-1]
        tm.assert_index_equal(ordered, expected)
        tm.assert_numpy_array_equal(indexer, np.array([2, 1, 0]), check_dtype=False)
        assert ordered.freq == expected.freq
        assert ordered.freq == freq
    idx1 = PeriodIndex(['2011-01-01', '2011-01-03', '2011-01-05', '2011-01-02', '2011-01-01'], freq='D', name='idx1')
    exp1 = PeriodIndex(['2011-01-01', '2011-01-01', '2011-01-02', '2011-01-03', '2011-01-05'], freq='D', name='idx1')
    idx2 = PeriodIndex(['2011-01-01', '2011-01-03', '2011-01-05', '2011-01-02', '2011-01-01'], freq='D', name='idx2')
    exp2 = PeriodIndex(['2011-01-01', '2011-01-01', '2011-01-02', '2011-01-03', '2011-01-05'], freq='D', name='idx2')
    idx3 = PeriodIndex([NaT, '2011-01-03', '2011-01-05', '2011-01-02', NaT], freq='D', name='idx3')
    exp3 = PeriodIndex([NaT, NaT, '2011-01-02', '2011-01-03', '2011-01-05'], freq='D', name='idx3')
    for idx, expected in [(idx1, exp1), (idx2, exp2), (idx3, exp3)]:
        ordered = idx.sort_values()
        tm.assert_index_equal(ordered, expected)
        assert ordered.freq == 'D'
        ordered = idx.sort_values(ascending=False)
        tm.assert_index_equal(ordered, expected[::-1])
        assert ordered.freq == 'D'
        ordered, indexer = idx.sort_values(return_indexer=True)
        tm.assert_index_equal(ordered, expected)
        exp = np.array([0, 4, 3, 1, 2])
        tm.assert_numpy_array_equal(indexer, exp, check_dtype=False)
        assert ordered.freq == 'D'
        ordered, indexer = idx.sort_values(return_indexer=True, ascending=False)
        tm.assert_index_equal(ordered, expected[::-1])
        exp = np.array([2, 1, 3, 4, 0])
        tm.assert_numpy_array_equal(indexer, exp, check_dtype=False)
        assert ordered.freq == 'D'