def test_getitem_arraylike_mask(self):
    arr = SparseArray([0, 1, 2])
    result = arr[[True, False, True]]
    expected = SparseArray([0, 2])
    tm.assert_sp_array_equal(result, expected)