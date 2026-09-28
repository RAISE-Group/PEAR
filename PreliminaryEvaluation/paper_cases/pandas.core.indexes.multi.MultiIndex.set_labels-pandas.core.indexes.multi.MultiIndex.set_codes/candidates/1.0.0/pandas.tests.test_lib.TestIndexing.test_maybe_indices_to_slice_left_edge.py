def test_maybe_indices_to_slice_left_edge(self):
    target = np.arange(100)
    indices = np.array([], dtype=np.int64)
    maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
    assert isinstance(maybe_slice, slice)
    tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
    for end in [1, 2, 5, 20, 99]:
        for step in [1, 2, 4]:
            indices = np.arange(0, end, step, dtype=np.int64)
            maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
            assert isinstance(maybe_slice, slice)
            tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
            indices = indices[::-1]
            maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
            assert isinstance(maybe_slice, slice)
            tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
    for case in [[2, 1, 2, 0], [2, 2, 1, 0], [0, 1, 2, 1], [-2, 0, 2], [2, 0, -2]]:
        indices = np.array(case, dtype=np.int64)
        maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
        assert not isinstance(maybe_slice, slice)
        tm.assert_numpy_array_equal(maybe_slice, indices)
        tm.assert_numpy_array_equal(target[indices], target[maybe_slice])