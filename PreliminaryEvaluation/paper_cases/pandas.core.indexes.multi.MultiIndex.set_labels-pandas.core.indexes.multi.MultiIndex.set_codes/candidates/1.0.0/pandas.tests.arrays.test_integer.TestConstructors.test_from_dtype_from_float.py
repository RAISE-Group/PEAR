def test_from_dtype_from_float(self, data):
    dtype = data.dtype
    expected = pd.Series(data)
    result = pd.Series(data.to_numpy(na_value=np.nan, dtype='float'), dtype=str(dtype))
    tm.assert_series_equal(result, expected)
    expected = pd.Series(data)
    result = pd.Series(np.array(data).tolist(), dtype=str(dtype))
    tm.assert_series_equal(result, expected)
    expected = pd.Series(data).dropna().reset_index(drop=True)
    dropped = np.array(data.dropna()).astype(np.dtype(dtype.type))
    result = pd.Series(dropped, dtype=str(dtype))
    tm.assert_series_equal(result, expected)