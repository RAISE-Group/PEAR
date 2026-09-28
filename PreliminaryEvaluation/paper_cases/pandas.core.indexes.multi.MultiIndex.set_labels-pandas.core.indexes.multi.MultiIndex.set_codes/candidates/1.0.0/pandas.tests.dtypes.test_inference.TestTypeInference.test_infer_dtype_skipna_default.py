def test_infer_dtype_skipna_default(self):
    arr = np.array([1, 2, 3, np.nan], dtype=object)
    result = lib.infer_dtype(arr)
    assert result == 'integer'