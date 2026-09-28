def test_reindex_axis(self):

    def assert_reindex_axis_is_ok(mgr, axis, new_labels, fill_value):
        mat = mgr.as_array()
        indexer = mgr.axes[axis].get_indexer_for(new_labels)
        reindexed = mgr.reindex_axis(new_labels, axis, fill_value=fill_value)
        tm.assert_numpy_array_equal(algos.take_nd(mat, indexer, axis, fill_value=fill_value), reindexed.as_array(), check_dtype=False)
        tm.assert_index_equal(reindexed.axes[axis], new_labels)
    for mgr in self.MANAGERS:
        for ax in range(mgr.ndim):
            for fill_value in (None, np.nan, 100.0):
                assert_reindex_axis_is_ok(mgr, ax, pd.Index([]), fill_value)
                assert_reindex_axis_is_ok(mgr, ax, mgr.axes[ax], fill_value)
                assert_reindex_axis_is_ok(mgr, ax, mgr.axes[ax][[0, 0, 0]], fill_value)
                assert_reindex_axis_is_ok(mgr, ax, pd.Index(['foo', 'bar', 'baz']), fill_value)
                assert_reindex_axis_is_ok(mgr, ax, pd.Index(['foo', mgr.axes[ax][0], 'baz']), fill_value)
                if mgr.shape[ax] >= 3:
                    assert_reindex_axis_is_ok(mgr, ax, mgr.axes[ax][:-3], fill_value)
                    assert_reindex_axis_is_ok(mgr, ax, mgr.axes[ax][-3::-1], fill_value)
                    assert_reindex_axis_is_ok(mgr, ax, mgr.axes[ax][[0, 1, 2, 0, 1, 2]], fill_value)