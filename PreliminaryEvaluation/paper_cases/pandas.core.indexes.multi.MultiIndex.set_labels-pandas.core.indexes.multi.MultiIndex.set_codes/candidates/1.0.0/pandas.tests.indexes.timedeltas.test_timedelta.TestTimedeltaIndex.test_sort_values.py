def test_sort_values(self):
    idx = TimedeltaIndex(['4d', '1d', '2d'])
    ordered = idx.sort_values()
    assert ordered.is_monotonic
    ordered = idx.sort_values(ascending=False)
    assert ordered[::-1].is_monotonic
    ordered, dexer = idx.sort_values(return_indexer=True)
    assert ordered.is_monotonic
    tm.assert_numpy_array_equal(dexer, np.array([1, 2, 0]), check_dtype=False)
    ordered, dexer = idx.sort_values(return_indexer=True, ascending=False)
    assert ordered[::-1].is_monotonic
    tm.assert_numpy_array_equal(dexer, np.array([0, 2, 1]), check_dtype=False)