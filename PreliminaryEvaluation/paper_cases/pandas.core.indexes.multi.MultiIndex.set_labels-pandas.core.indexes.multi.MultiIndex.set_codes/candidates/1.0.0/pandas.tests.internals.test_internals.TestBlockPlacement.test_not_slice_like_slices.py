def test_not_slice_like_slices(self):

    def assert_not_slice_like(slc):
        assert not BlockPlacement(slc).is_slice_like
    assert_not_slice_like(slice(0, 0))
    assert_not_slice_like(slice(100, 0))
    assert_not_slice_like(slice(100, 100, -1))
    assert_not_slice_like(slice(0, 100, -1))
    assert not BlockPlacement(slice(0, 0)).is_slice_like
    assert not BlockPlacement(slice(100, 100)).is_slice_like