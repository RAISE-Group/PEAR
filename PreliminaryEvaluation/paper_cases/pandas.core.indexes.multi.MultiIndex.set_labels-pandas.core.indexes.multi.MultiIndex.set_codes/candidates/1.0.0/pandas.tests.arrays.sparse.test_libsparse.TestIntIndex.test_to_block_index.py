def test_to_block_index(self):

    def _check_case(xloc, xlen, yloc, ylen, eloc, elen):
        xindex = BlockIndex(TEST_LENGTH, xloc, xlen)
        yindex = BlockIndex(TEST_LENGTH, yloc, ylen)
        xbindex = xindex.to_int_index().to_block_index()
        ybindex = yindex.to_int_index().to_block_index()
        assert isinstance(xbindex, BlockIndex)
        assert xbindex.equals(xindex)
        assert ybindex.equals(yindex)
    check_cases(_check_case)