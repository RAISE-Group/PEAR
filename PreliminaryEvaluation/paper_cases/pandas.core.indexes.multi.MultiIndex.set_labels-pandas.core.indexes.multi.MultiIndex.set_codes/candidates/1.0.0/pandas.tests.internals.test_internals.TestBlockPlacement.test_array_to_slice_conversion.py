def test_array_to_slice_conversion(self):

    def assert_as_slice_equals(arr, slc):
        assert BlockPlacement(arr).as_slice == slc
    assert_as_slice_equals([0], slice(0, 1, 1))
    assert_as_slice_equals([100], slice(100, 101, 1))
    assert_as_slice_equals([0, 1, 2], slice(0, 3, 1))
    assert_as_slice_equals([0, 5, 10], slice(0, 15, 5))
    assert_as_slice_equals([0, 100], slice(0, 200, 100))
    assert_as_slice_equals([2, 1], slice(2, 0, -1))