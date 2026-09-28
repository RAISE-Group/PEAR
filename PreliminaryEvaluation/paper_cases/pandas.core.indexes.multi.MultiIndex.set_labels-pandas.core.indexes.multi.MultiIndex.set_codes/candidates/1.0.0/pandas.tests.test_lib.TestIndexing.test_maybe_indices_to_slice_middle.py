def test_maybe_indices_to_slice_middle(self):
    target = np.arange(100)
    for start, end in [(2, 10), (5, 25), (65, 97)]:
        for step in [1, 2, 4, 20]:
            indices = np.arange(start, end, step, dtype=np.int64)
            maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
            assert isinstance(maybe_slice, slice)
            tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
            indices = indices[::-1]
            maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
            assert isinstance(maybe_slice, slice)
            tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
    for case in [[14, 12, 10, 12], [12, 12, 11, 10], [10, 11, 12, 11]]:
        indices = np.array(case, dtype=np.int64)
        maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
        assert not isinstance(maybe_slice, slice)
        tm.assert_numpy_array_equal(maybe_slice, indices)
        tm.assert_numpy_array_equal(target[indices], target[maybe_slice])