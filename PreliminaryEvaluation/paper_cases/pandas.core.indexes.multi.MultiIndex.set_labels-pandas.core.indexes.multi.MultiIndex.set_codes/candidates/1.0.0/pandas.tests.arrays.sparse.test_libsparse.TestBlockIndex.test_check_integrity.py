def test_check_integrity(self):
    locs = []
    lengths = []
    index = BlockIndex(0, locs, lengths)
    index = BlockIndex(1, locs, lengths)
    msg = 'Block 0 extends beyond end'
    with pytest.raises(ValueError, match=msg):
        BlockIndex(10, [5], [10])
    msg = 'Block 0 overlaps'
    with pytest.raises(ValueError, match=msg):
        BlockIndex(10, [2, 5], [5, 3])