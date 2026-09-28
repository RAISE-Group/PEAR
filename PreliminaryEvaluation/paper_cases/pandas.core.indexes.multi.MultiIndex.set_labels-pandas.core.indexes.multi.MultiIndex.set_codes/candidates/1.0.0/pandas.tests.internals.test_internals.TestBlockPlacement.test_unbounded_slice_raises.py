def test_unbounded_slice_raises(self):

    def assert_unbounded_slice_error(slc):
        with pytest.raises(ValueError, match='unbounded slice'):
            BlockPlacement(slc)
    assert_unbounded_slice_error(slice(None, None))
    assert_unbounded_slice_error(slice(10, None))
    assert_unbounded_slice_error(slice(None, None, -1))
    assert_unbounded_slice_error(slice(None, 10, -1))
    assert_unbounded_slice_error(slice(-1, None))
    assert_unbounded_slice_error(slice(None, -1))
    assert_unbounded_slice_error(slice(-1, -1))
    assert_unbounded_slice_error(slice(-1, None, -1))
    assert_unbounded_slice_error(slice(None, -1, -1))
    assert_unbounded_slice_error(slice(-1, -1, -1))