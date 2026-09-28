def test_mgr_locs(self):
    assert isinstance(self.fblock.mgr_locs, BlockPlacement)
    tm.assert_numpy_array_equal(self.fblock.mgr_locs.as_array, np.array([0, 2, 4], dtype=np.int64))