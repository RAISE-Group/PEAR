def test_to_block_index(self):
    index = BlockIndex(10, [0, 5], [4, 5])
    assert index.to_block_index() is index