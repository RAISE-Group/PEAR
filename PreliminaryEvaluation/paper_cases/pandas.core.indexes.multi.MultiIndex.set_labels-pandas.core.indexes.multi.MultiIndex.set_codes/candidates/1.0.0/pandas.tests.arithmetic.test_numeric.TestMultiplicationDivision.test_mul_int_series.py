def test_mul_int_series(self, numeric_idx):
    idx = numeric_idx
    didx = idx * idx
    arr_dtype = 'uint64' if isinstance(idx, pd.UInt64Index) else 'int64'
    result = idx * Series(np.arange(5, dtype=arr_dtype))
    tm.assert_series_equal(result, Series(didx))