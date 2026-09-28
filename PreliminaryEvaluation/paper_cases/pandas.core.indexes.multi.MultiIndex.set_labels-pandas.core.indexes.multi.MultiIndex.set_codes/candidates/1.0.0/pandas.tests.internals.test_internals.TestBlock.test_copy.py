def test_copy(self):
    cop = self.fblock.copy()
    assert cop is not self.fblock
    assert_block_equal(self.fblock, cop)