def test_object(self):
    arr = np.array([None], dtype='O')
    result = lib.infer_dtype(arr, skipna=False)
    assert result == 'mixed'
    result = lib.infer_dtype(arr, skipna=True)
    assert result == 'empty'