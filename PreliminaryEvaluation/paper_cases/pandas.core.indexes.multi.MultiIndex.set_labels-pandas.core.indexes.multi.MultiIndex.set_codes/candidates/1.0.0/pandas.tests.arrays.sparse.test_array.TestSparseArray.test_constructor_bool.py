def test_constructor_bool(self):
    data = np.array([False, False, True, True, False, False])
    arr = SparseArray(data, fill_value=False, dtype=bool)
    assert arr.dtype == SparseDtype(bool)
    tm.assert_numpy_array_equal(arr.sp_values, np.array([True, True]))
    tm.assert_numpy_array_equal(arr.sp_index.indices, np.array([2, 3], np.int32))
    dense = arr.to_dense()
    assert dense.dtype == bool
    tm.assert_numpy_array_equal(dense, data)