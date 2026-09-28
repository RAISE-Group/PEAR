def test_equals(self):
    index = BlockIndex(10, [0, 4], [2, 5])
    assert index.equals(index)
    assert not index.equals(BlockIndex(10, [0, 4], [2, 6]))