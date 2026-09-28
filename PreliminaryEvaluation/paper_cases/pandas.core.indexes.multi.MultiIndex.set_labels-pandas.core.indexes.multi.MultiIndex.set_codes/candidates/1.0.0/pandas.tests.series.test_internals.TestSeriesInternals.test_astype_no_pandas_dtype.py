def test_astype_no_pandas_dtype(self):
    ser = pd.Series([1, 2], dtype='int64')
    result = ser.astype(ser.array.dtype)
    tm.assert_series_equal(result, ser)