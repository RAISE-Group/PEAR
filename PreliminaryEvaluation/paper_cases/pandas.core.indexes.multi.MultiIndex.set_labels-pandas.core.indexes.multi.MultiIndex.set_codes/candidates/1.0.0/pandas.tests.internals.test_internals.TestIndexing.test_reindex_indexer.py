def test_reindex_indexer(self):

    def assert_reindex_indexer_is_ok(mgr, axis, new_labels, indexer, fill_value):
        mat = mgr.as_array()
        reindexed_mat = algos.take_nd(mat, indexer, axis, fill_value=fill_value)
        reindexed = mgr.reindex_indexer(new_labels, indexer, axis, fill_value=fill_value)
        tm.assert_numpy_array_equal(reindexed_mat, reindexed.as_array(), check_dtype=False)
        tm.assert_index_equal(reindexed.axes[axis], new_labels)
    for mgr in self.MANAGERS:
        for ax in range(mgr.ndim):
            for fill_value in (None, np.nan, 100.0):
                assert_reindex_indexer_is_ok(mgr, ax, pd.Index([]), [], fill_value)
                assert_reindex_indexer_is_ok(mgr, ax, mgr.axes[ax], np.arange(mgr.shape[ax]), fill_value)
                assert_reindex_indexer_is_ok(mgr, ax, pd.Index(['foo'] * mgr.shape[ax]), np.arange(mgr.shape[ax]), fill_value)
                assert_reindex_indexer_is_ok(mgr, ax, mgr.axes[ax][::-1], np.arange(mgr.shape[ax]), fill_value)
                assert_reindex_indexer_is_ok(mgr, ax, mgr.axes[ax], np.arange(mgr.shape[ax])[::-1], fill_value)
                assert_reindex_indexer_is_ok(mgr, ax, pd.Index(['foo', 'bar', 'baz']), [0, 0, 0], fill_value)
                assert_reindex_indexer_is_ok(mgr, ax, pd.Index(['foo', 'bar', 'baz']), [-1, 0, -1], fill_value)
                assert_reindex_indexer_is_ok(mgr, ax, pd.Index(['foo', mgr.axes[ax][0], 'baz']), [-1, -1, -1], fill_value)
                if mgr.shape[ax] >= 3:
                    assert_reindex_indexer_is_ok(mgr, ax, pd.Index(['foo', 'bar', 'baz']), [0, 1, 2], fill_value)