def test_constructor_bool_fill_value(self):
    arr = SparseArray([True, False, True], dtype=None)
    assert arr.dtype == SparseDtype(np.bool)
    assert not arr.fill_value
    arr = SparseArray([True, False, True], dtype=np.bool)
    assert arr.dtype == SparseDtype(np.bool)
    assert not arr.fill_value
    arr = SparseArray([True, False, True], dtype=np.bool, fill_value=True)
    assert arr.dtype == SparseDtype(np.bool, True)
    assert arr.fill_value