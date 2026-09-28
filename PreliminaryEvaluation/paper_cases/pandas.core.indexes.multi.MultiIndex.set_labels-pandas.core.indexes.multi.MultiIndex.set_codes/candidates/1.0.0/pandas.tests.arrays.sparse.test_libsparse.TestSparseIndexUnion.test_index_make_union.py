def test_index_make_union(self):

    def _check_case(xloc, xlen, yloc, ylen, eloc, elen):
        xindex = BlockIndex(TEST_LENGTH, xloc, xlen)
        yindex = BlockIndex(TEST_LENGTH, yloc, ylen)
        bresult = xindex.make_union(yindex)
        assert isinstance(bresult, BlockIndex)
        tm.assert_numpy_array_equal(bresult.blocs, np.array(eloc, dtype=np.int32))
        tm.assert_numpy_array_equal(bresult.blengths, np.array(elen, dtype=np.int32))
        ixindex = xindex.to_int_index()
        iyindex = yindex.to_int_index()
        iresult = ixindex.make_union(iyindex)
        assert isinstance(iresult, IntIndex)
        tm.assert_numpy_array_equal(iresult.indices, bresult.to_int_index().indices)
    '\n        x: ----\n        y:     ----\n        r: --------\n        '
    xloc = [0]
    xlen = [5]
    yloc = [5]
    ylen = [4]
    eloc = [0]
    elen = [9]
    _check_case(xloc, xlen, yloc, ylen, eloc, elen)
    '\n        x: -----     -----\n        y:   -----          --\n        '
    xloc = [0, 10]
    xlen = [5, 5]
    yloc = [2, 17]
    ylen = [5, 2]
    eloc = [0, 10, 17]
    elen = [7, 5, 2]
    _check_case(xloc, xlen, yloc, ylen, eloc, elen)
    '\n        x: ------\n        y:    -------\n        r: ----------\n        '
    xloc = [1]
    xlen = [5]
    yloc = [3]
    ylen = [5]
    eloc = [1]
    elen = [7]
    _check_case(xloc, xlen, yloc, ylen, eloc, elen)
    '\n        x: ------  -----\n        y:    -------\n        r: -------------\n        '
    xloc = [2, 10]
    xlen = [4, 4]
    yloc = [4]
    ylen = [8]
    eloc = [2]
    elen = [12]
    _check_case(xloc, xlen, yloc, ylen, eloc, elen)
    '\n        x: ---  -----\n        y: -------\n        r: -------------\n        '
    xloc = [0, 5]
    xlen = [3, 5]
    yloc = [0]
    ylen = [7]
    eloc = [0]
    elen = [10]
    _check_case(xloc, xlen, yloc, ylen, eloc, elen)
    '\n        x: ------  -----\n        y:    -------  ---\n        r: -------------\n        '
    xloc = [2, 10]
    xlen = [4, 4]
    yloc = [4, 13]
    ylen = [8, 4]
    eloc = [2]
    elen = [15]
    _check_case(xloc, xlen, yloc, ylen, eloc, elen)
    '\n        x: ----------------------\n        y:   ----  ----   ---\n        r: ----------------------\n        '
    xloc = [2]
    xlen = [15]
    yloc = [4, 9, 14]
    ylen = [3, 2, 2]
    eloc = [2]
    elen = [15]
    _check_case(xloc, xlen, yloc, ylen, eloc, elen)
    '\n        x: ----       ---\n        y:       ---       ---\n        '
    xloc = [0, 10]
    xlen = [3, 3]
    yloc = [5, 15]
    ylen = [2, 2]
    eloc = [0, 5, 10, 15]
    elen = [3, 2, 3, 2]
    _check_case(xloc, xlen, yloc, ylen, eloc, elen)