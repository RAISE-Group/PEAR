@pytest.mark.parametrize('sparse_index', [None, IntIndex(1, [0])])
def test_constructor_spindex_dtype_scalar(self, sparse_index):
    arr = SparseArray(data=1, sparse_index=sparse_index, dtype=None)
    exp = SparseArray([1], dtype=None)
    tm.assert_sp_array_equal(arr, exp)
    assert arr.dtype == SparseDtype(np.int64)
    assert arr.fill_value == 0
    arr = SparseArray(data=1, sparse_index=IntIndex(1, [0]), dtype=None)
    exp = SparseArray([1], dtype=None)
    tm.assert_sp_array_equal(arr, exp)
    assert arr.dtype == SparseDtype(np.int64)
    assert arr.fill_value == 0