def test_astype_bool(self):
    a = SparseArray([1, 0, 0, 1], dtype=SparseDtype(int, 0))
    result = a.astype(bool)
    expected = SparseArray([True, 0, 0, True], dtype=SparseDtype(bool, 0))
    tm.assert_sp_array_equal(result, expected)
    result = a.astype(SparseDtype(bool, False))
    expected = SparseArray([True, False, False, True], dtype=SparseDtype(bool, False))
    tm.assert_sp_array_equal(result, expected)