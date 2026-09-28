def test_get_slice(self):

    def assert_slice_ok(mgr, axis, slobj):
        mat = mgr.as_array()
        if isinstance(slobj, np.ndarray):
            ax = mgr.axes[axis]
            if len(ax) and len(slobj) and (len(slobj) != len(ax)):
                slobj = np.concatenate([slobj, np.zeros(len(ax) - len(slobj), dtype=bool)])
        sliced = mgr.get_slice(slobj, axis=axis)
        mat_slobj = (slice(None),) * axis + (slobj,)
        tm.assert_numpy_array_equal(mat[mat_slobj], sliced.as_array(), check_dtype=False)
        tm.assert_index_equal(mgr.axes[axis][slobj], sliced.axes[axis])
    for mgr in self.MANAGERS:
        for ax in range(mgr.ndim):
            assert_slice_ok(mgr, ax, slice(None))
            assert_slice_ok(mgr, ax, slice(3))
            assert_slice_ok(mgr, ax, slice(100))
            assert_slice_ok(mgr, ax, slice(1, 4))
            assert_slice_ok(mgr, ax, slice(3, 0, -2))
            assert_slice_ok(mgr, ax, np.array([], dtype=np.bool_))
            assert_slice_ok(mgr, ax, np.ones(mgr.shape[ax], dtype=np.bool_))
            assert_slice_ok(mgr, ax, np.zeros(mgr.shape[ax], dtype=np.bool_))
            if mgr.shape[ax] >= 3:
                assert_slice_ok(mgr, ax, np.arange(mgr.shape[ax]) % 3 == 0)
                assert_slice_ok(mgr, ax, np.array([True, True, False], dtype=np.bool_))
            assert_slice_ok(mgr, ax, [])
            assert_slice_ok(mgr, ax, list(range(mgr.shape[ax])))
            if mgr.shape[ax] >= 3:
                assert_slice_ok(mgr, ax, [0, 1, 2])
                assert_slice_ok(mgr, ax, [-1, -2, -3])