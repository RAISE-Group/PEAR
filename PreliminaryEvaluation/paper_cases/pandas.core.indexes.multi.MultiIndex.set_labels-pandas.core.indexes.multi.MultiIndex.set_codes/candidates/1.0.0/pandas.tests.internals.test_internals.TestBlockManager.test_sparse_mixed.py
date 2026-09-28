def test_sparse_mixed(self):
    mgr = create_mgr('a: sparse-1; b: sparse-2; c: f8')
    assert len(mgr.blocks) == 3
    assert isinstance(mgr, BlockManager)