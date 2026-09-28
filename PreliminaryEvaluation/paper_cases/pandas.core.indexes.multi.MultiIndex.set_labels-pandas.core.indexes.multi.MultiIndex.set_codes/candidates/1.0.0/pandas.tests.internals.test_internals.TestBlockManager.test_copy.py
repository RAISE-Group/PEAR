def test_copy(self, mgr):
    cp = mgr.copy(deep=False)
    for blk, cp_blk in zip(mgr.blocks, cp.blocks):
        assert cp_blk.equals(blk)
        if isinstance(blk.values, np.ndarray):
            assert cp_blk.values.base is blk.values.base
        else:
            assert cp_blk.values._data.base is blk.values._data.base
    cp = mgr.copy(deep=True)
    for blk, cp_blk in zip(mgr.blocks, cp.blocks):
        assert cp_blk.equals(blk)
        if not isinstance(cp_blk.values, np.ndarray):
            assert cp_blk.values._data.base is not blk.values._data.base
        else:
            assert cp_blk.values.base is None and blk.values.base is None