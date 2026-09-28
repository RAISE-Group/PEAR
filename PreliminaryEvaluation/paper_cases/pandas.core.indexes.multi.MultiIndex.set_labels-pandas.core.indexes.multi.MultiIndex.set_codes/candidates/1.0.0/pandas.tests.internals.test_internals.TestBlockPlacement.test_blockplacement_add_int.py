def test_blockplacement_add_int(self):

    def assert_add_equals(val, inc, result):
        assert list(BlockPlacement(val).add(inc)) == result
    assert_add_equals(slice(0, 0), 0, [])
    assert_add_equals(slice(1, 4), 0, [1, 2, 3])
    assert_add_equals(slice(3, 0, -1), 0, [3, 2, 1])
    assert_add_equals([1, 2, 4], 0, [1, 2, 4])
    assert_add_equals(slice(0, 0), 10, [])
    assert_add_equals(slice(1, 4), 10, [11, 12, 13])
    assert_add_equals(slice(3, 0, -1), 10, [13, 12, 11])
    assert_add_equals([1, 2, 4], 10, [11, 12, 14])
    assert_add_equals(slice(0, 0), -1, [])
    assert_add_equals(slice(1, 4), -1, [0, 1, 2])
    assert_add_equals([1, 2, 4], -1, [0, 1, 3])
    with pytest.raises(ValueError):
        BlockPlacement(slice(1, 4)).add(-10)
    with pytest.raises(ValueError):
        BlockPlacement([1, 2, 4]).add(-10)