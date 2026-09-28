@pytest.mark.parametrize('idx', [DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'], freq='D', name='idx'), DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], freq='H', name='tzidx', tz='Asia/Tokyo')])
def test_order_with_freq(self, idx):
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
    expected = idx[::-1]
    tm.assert_index_equal(ordered, expected)
    tm.assert_numpy_array_equal(indexer, np.array([2, 1, 0]), check_dtype=False)
    assert ordered.freq == expected.freq
    assert ordered.freq.n == -1