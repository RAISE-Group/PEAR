def test_duplicate_ref_loc_failure(self):
    tmp_mgr = create_mgr('a:bool; a: f8')
    axes, blocks = (tmp_mgr.axes, tmp_mgr.blocks)
    blocks[0].mgr_locs = np.array([0])
    blocks[1].mgr_locs = np.array([0])
    with pytest.raises(AssertionError):
        BlockManager(blocks, axes)
    blocks[0].mgr_locs = np.array([0])
    blocks[1].mgr_locs = np.array([1])
    mgr = BlockManager(blocks, axes)
    mgr.iget(1)