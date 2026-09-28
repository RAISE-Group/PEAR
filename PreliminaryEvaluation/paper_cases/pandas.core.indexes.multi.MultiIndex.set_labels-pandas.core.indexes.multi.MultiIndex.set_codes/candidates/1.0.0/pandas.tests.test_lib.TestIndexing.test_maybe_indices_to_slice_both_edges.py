def test_maybe_indices_to_slice_both_edges(self):
    target = np.arange(10)
    for step in [1, 2, 4, 5, 8, 9]:
        indices = np.arange(0, 9, step, dtype=np.int64)
        maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
        assert isinstance(maybe_slice, slice)
        tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
        indices = indices[::-1]
        maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
        assert isinstance(maybe_slice, slice)
        tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
    for case in [[4, 2, 0, -2], [2, 2, 1, 0], [0, 1, 2, 1]]:
        indices = np.array(case, dtype=np.int64)
        maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
        assert not isinstance(maybe_slice, slice)
        tm.assert_numpy_array_equal(maybe_slice, indices)
        tm.assert_numpy_array_equal(target[indices], target[maybe_slice])