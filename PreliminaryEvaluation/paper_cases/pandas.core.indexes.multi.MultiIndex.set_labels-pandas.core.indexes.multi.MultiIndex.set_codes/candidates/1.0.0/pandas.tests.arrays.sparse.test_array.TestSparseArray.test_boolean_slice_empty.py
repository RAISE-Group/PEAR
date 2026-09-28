def test_boolean_slice_empty(self):
    arr = SparseArray([0, 1, 2])
    res = arr[[False, False, False]]
    assert res.dtype == arr.dtype