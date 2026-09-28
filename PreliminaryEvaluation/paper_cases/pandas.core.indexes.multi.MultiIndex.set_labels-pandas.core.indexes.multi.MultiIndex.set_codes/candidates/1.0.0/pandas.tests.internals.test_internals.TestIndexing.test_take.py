def test_take(self):

    def assert_take_ok(mgr, axis, indexer):
        mat = mgr.as_array()
        taken = mgr.take(indexer, axis)
        tm.assert_numpy_array_equal(np.take(mat, indexer, axis), taken.as_array(), check_dtype=False)
        tm.assert_index_equal(mgr.axes[axis].take(indexer), taken.axes[axis])
    for mgr in self.MANAGERS:
        for ax in range(mgr.ndim):
            assert_take_ok(mgr, ax, indexer=[])
            assert_take_ok(mgr, ax, indexer=[0, 0, 0])
            assert_take_ok(mgr, ax, indexer=list(range(mgr.shape[ax])))
            if mgr.shape[ax] >= 3:
                assert_take_ok(mgr, ax, indexer=[0, 1, 2])
                assert_take_ok(mgr, ax, indexer=[-1, -2, -3])