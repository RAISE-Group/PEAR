def test_categorical(self):
    arr = Categorical(list('abc'))
    result = lib.infer_dtype(arr, skipna=True)
    assert result == 'categorical'
    result = lib.infer_dtype(Series(arr), skipna=True)
    assert result == 'categorical'
    arr = Categorical(list('abc'), categories=['cegfab'], ordered=True)
    result = lib.infer_dtype(arr, skipna=True)
    assert result == 'categorical'
    result = lib.infer_dtype(Series(arr), skipna=True)
    assert result == 'categorical'