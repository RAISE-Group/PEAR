def test_unicode(self):
    arr = ['a', np.nan, 'c']
    result = lib.infer_dtype(arr, skipna=False)
    assert result == 'mixed'
    arr = ['a', np.nan, 'c']
    result = lib.infer_dtype(arr, skipna=True)
    assert result == 'string'
    arr = ['a', 'c']
    result = lib.infer_dtype(arr, skipna=False)
    assert result == 'string'