@pytest.mark.parametrize('scalar,dtype', [(False, SparseDtype(bool, False)), (0.0, SparseDtype('float64', 0)), (1, SparseDtype('int64', 1)), ('z', SparseDtype('object', 'z'))])
def test_scalar_with_index_infer_dtype(self, scalar, dtype):
    arr = SparseArray(scalar, index=[1, 2, 3], fill_value=scalar)
    exp = SparseArray([scalar, scalar, scalar], fill_value=scalar)
    tm.assert_sp_array_equal(arr, exp)
    assert arr.dtype == dtype
    assert exp.dtype == dtype