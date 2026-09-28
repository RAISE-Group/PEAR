def test_constructor_object_dtype(self):
    arr = SparseArray(['A', 'A', np.nan, 'B'], dtype=np.object)
    assert arr.dtype == SparseDtype(np.object)
    assert np.isnan(arr.fill_value)
    arr = SparseArray(['A', 'A', np.nan, 'B'], dtype=np.object, fill_value='A')
    assert arr.dtype == SparseDtype(np.object, 'A')
    assert arr.fill_value == 'A'
    data = [False, 0, 100.0, 0.0]
    arr = SparseArray(data, dtype=np.object, fill_value=False)
    assert arr.dtype == SparseDtype(np.object, False)
    assert arr.fill_value is False
    arr_expected = np.array(data, dtype=np.object)
    it = (type(x) == type(y) and x == y for x, y in zip(arr, arr_expected))
    assert np.fromiter(it, dtype=np.bool).all()