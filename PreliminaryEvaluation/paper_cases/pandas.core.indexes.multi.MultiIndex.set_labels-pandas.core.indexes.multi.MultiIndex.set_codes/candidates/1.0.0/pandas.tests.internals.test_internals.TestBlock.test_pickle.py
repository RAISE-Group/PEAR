def test_pickle(self):

    def _check(blk):
        assert_block_equal(tm.round_trip_pickle(blk), blk)
    _check(self.fblock)
    _check(self.cblock)
    _check(self.oblock)
    _check(self.bool_block)