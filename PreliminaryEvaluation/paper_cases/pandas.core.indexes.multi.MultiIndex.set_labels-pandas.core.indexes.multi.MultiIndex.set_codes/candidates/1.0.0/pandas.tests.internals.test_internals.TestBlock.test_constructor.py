def test_constructor(self):
    int32block = create_block('i4', [0])
    assert int32block.dtype == np.int32