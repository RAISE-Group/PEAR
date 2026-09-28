@td.skip_if_windows
def test_intersect(self):

    def _check_correct(a, b, expected):
        result = a.intersect(b)
        assert result.equals(expected)

    def _check_length_exc(a, longer):
        msg = 'Indices must reference same underlying length'
        with pytest.raises(Exception, match=msg):
            a.intersect(longer)

    def _check_case(xloc, xlen, yloc, ylen, eloc, elen):
        xindex = BlockIndex(TEST_LENGTH, xloc, xlen)
        yindex = BlockIndex(TEST_LENGTH, yloc, ylen)
        expected = BlockIndex(TEST_LENGTH, eloc, elen)
        longer_index = BlockIndex(TEST_LENGTH + 1, yloc, ylen)
        _check_correct(xindex, yindex, expected)
        _check_correct(xindex.to_int_index(), yindex.to_int_index(), expected.to_int_index())
        _check_length_exc(xindex, longer_index)
        _check_length_exc(xindex.to_int_index(), longer_index.to_int_index())
    check_cases(_check_case)