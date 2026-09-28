def test_not_slice_like_arrays(self):

    def assert_not_slice_like(arr):
        assert not BlockPlacement(arr).is_slice_like
    assert_not_slice_like([])
    assert_not_slice_like([-1])
    assert_not_slice_like([-1, -2, -3])
    assert_not_slice_like([-10])
    assert_not_slice_like([-1])
    assert_not_slice_like([-1, 0, 1, 2])
    assert_not_slice_like([-2, 0, 2, 4])
    assert_not_slice_like([1, 0, -1])
    assert_not_slice_like([1, 1, 1])