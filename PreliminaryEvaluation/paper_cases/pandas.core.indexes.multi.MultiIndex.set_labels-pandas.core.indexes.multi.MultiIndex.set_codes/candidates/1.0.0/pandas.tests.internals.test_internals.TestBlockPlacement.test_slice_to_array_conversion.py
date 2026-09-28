def test_slice_to_array_conversion(self):

    def assert_as_array_equals(slc, asarray):
        tm.assert_numpy_array_equal(BlockPlacement(slc).as_array, np.asarray(asarray, dtype=np.int64))
    assert_as_array_equals(slice(0, 3), [0, 1, 2])
    assert_as_array_equals(slice(0, 0), [])
    assert_as_array_equals(slice(3, 0), [])
    assert_as_array_equals(slice(3, 0, -1), [3, 2, 1])