def test_slice_iter(self):
    assert list(BlockPlacement(slice(0, 3))) == [0, 1, 2]
    assert list(BlockPlacement(slice(0, 0))) == []
    assert list(BlockPlacement(slice(3, 0))) == []