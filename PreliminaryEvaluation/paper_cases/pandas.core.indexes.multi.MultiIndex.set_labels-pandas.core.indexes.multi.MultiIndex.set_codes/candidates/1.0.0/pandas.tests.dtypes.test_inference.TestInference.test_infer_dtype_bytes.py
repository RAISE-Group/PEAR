def test_infer_dtype_bytes(self):
    compare = 'bytes'
    arr = np.array(list('abc'), dtype='S1')
    assert lib.infer_dtype(arr, skipna=True) == compare
    arr = arr.astype(object)
    assert lib.infer_dtype(arr, skipna=True) == compare
    assert lib.infer_dtype([b'a', np.nan, b'c'], skipna=True) == compare