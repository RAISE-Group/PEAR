def test_set_fill_value(self):
    arr = SparseArray([1.0, np.nan, 2.0], fill_value=np.nan)
    arr.fill_value = 2
    assert arr.fill_value == 2
    arr = SparseArray([1, 0, 2], fill_value=0, dtype=np.int64)
    arr.fill_value = 2
    assert arr.fill_value == 2
    arr.fill_value = 3.1
    assert arr.fill_value == 3.1
    arr.fill_value = np.nan
    assert np.isnan(arr.fill_value)
    arr = SparseArray([True, False, True], fill_value=False, dtype=np.bool)
    arr.fill_value = True
    assert arr.fill_value
    arr.fill_value = 0
    assert arr.fill_value == 0
    arr.fill_value = np.nan
    assert np.isnan(arr.fill_value)