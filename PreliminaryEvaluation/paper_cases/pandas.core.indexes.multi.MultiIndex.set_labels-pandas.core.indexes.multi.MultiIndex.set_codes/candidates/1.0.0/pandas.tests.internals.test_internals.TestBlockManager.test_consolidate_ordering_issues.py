def test_consolidate_ordering_issues(self, mgr):
    mgr.set('f', tm.randn(N))
    mgr.set('d', tm.randn(N))
    mgr.set('b', tm.randn(N))
    mgr.set('g', tm.randn(N))
    mgr.set('h', tm.randn(N))
    cons = mgr.consolidate()
    assert cons.nblocks == 4
    cons = mgr.consolidate().get_numeric_data()
    assert cons.nblocks == 1
    assert isinstance(cons.blocks[0].mgr_locs, BlockPlacement)
    tm.assert_numpy_array_equal(cons.blocks[0].mgr_locs.as_array, np.arange(len(cons.items), dtype=np.int64))