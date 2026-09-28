def test_slice_len(self):
    assert len(BlockPlacement(slice(0, 4))) == 4
    assert len(BlockPlacement(slice(0, 4, 2))) == 2
    assert len(BlockPlacement(slice(0, 3, 2))) == 2
    assert len(BlockPlacement(slice(0, 1, 2))) == 1
    assert len(BlockPlacement(slice(1, 0, -1))) == 1