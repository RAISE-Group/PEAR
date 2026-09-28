def test_order(self):
    idx1 = TimedeltaIndex(['1 day', '2 day', '3 day'], freq='D', name='idx')
    idx2 = TimedeltaIndex(['1 hour', '2 hour', '3 hour'], freq='H', name='idx')
    for idx in [idx1, idx2]:
        ordered = idx.sort_values()
        tm.assert_index_equal(ordered, idx)
        assert ordered.freq == idx.freq
        ordered = idx.sort_values(ascending=False)
        expected = idx[::-1]
        tm.assert_index_equal(ordered, expected)
        assert ordered.freq == expected.freq
        assert ordered.freq.n == -1
        ordered, indexer = idx.sort_values(return_indexer=True)
        tm.assert_index_equal(ordered, idx)
        tm.assert_numpy_array_equal(indexer, np.array([0, 1, 2]), check_dtype=False)
        assert ordered.freq == idx.freq
        ordered, indexer = idx.sort_values(return_indexer=True, ascending=False)
        tm.assert_index_equal(ordered, idx[::-1])
        assert ordered.freq == expected.freq
        assert ordered.freq.n == -1
    idx1 = TimedeltaIndex(['1 hour', '3 hour', '5 hour', '2 hour ', '1 hour'], name='idx1')
    exp1 = TimedeltaIndex(['1 hour', '1 hour', '2 hour', '3 hour', '5 hour'], name='idx1')
    idx2 = TimedeltaIndex(['1 day', '3 day', '5 day', '2 day', '1 day'], name='idx2')
    for idx, expected in [(idx1, exp1), (idx1, exp1), (idx1, exp1)]:
        ordered = idx.sort_values()
        tm.assert_index_equal(ordered, expected)
        assert ordered.freq is None
        ordered = idx.sort_values(ascending=False)
        tm.assert_index_equal(ordered, expected[::-1])
        assert ordered.freq is None
        ordered, indexer = idx.sort_values(return_indexer=True)
        tm.assert_index_equal(ordered, expected)
        exp = np.array([0, 4, 3, 1, 2])
        tm.assert_numpy_array_equal(indexer, exp, check_dtype=False)
        assert ordered.freq is None
        ordered, indexer = idx.sort_values(return_indexer=True, ascending=False)
        tm.assert_index_equal(ordered, expected[::-1])
        exp = np.array([2, 1, 3, 4, 0])
        tm.assert_numpy_array_equal(indexer, exp, check_dtype=False)
        assert ordered.freq is None