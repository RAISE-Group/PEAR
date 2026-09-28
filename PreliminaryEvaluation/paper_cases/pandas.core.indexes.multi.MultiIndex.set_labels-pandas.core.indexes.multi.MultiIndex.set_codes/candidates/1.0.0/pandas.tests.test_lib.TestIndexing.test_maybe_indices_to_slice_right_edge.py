def test_maybe_indices_to_slice_right_edge(self):
    target = np.arange(100)
    for start in [0, 2, 5, 20, 97, 98]:
        for step in [1, 2, 4]:
            indices = np.arange(start, 99, step, dtype=np.int64)
            maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
            assert isinstance(maybe_slice, slice)
            tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
            indices = indices[::-1]
            maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
            assert isinstance(maybe_slice, slice)
            tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
    indices = np.array([97, 98, 99, 100], dtype=np.int64)
    maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
    assert not isinstance(maybe_slice, slice)
    tm.assert_numpy_array_equal(maybe_slice, indices)
    with pytest.raises(IndexError):
        target[indices]
    with pytest.raises(IndexError):
        target[maybe_slice]
    indices = np.array([100, 99, 98, 97], dtype=np.int64)
    maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
    assert not isinstance(maybe_slice, slice)
    tm.assert_numpy_array_equal(maybe_slice, indices)
    with pytest.raises(IndexError):
        target[indices]
    with pytest.raises(IndexError):
        target[maybe_slice]
    for case in [[99, 97, 99, 96], [99, 99, 98, 97], [98, 98, 97, 96]]:
        indices = np.array(case, dtype=np.int64)
        maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
        assert not isinstance(maybe_slice, slice)
        tm.assert_numpy_array_equal(maybe_slice, indices)
        tm.assert_numpy_array_equal(target[indices], target[maybe_slice])