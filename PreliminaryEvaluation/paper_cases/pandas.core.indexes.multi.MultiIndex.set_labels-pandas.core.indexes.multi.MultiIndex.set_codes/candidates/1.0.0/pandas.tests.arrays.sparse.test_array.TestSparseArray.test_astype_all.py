def test_astype_all(self, any_real_dtype):
    vals = np.array([1, 2, 3])
    arr = SparseArray(vals, fill_value=1)
    typ = np.dtype(any_real_dtype)
    res = arr.astype(typ)
    assert res.dtype == SparseDtype(typ, 1)
    assert res.sp_values.dtype == typ
    tm.assert_numpy_array_equal(np.asarray(res.to_dense()), vals.astype(typ))