def test_constructor_dtype_str_na_values(self, string_dtype):
    ser = Series(['x', None], dtype=string_dtype)
    result = ser.isna()
    expected = Series([False, True])
    tm.assert_series_equal(result, expected)
    assert ser.iloc[1] is None
    ser = Series(['x', np.nan], dtype=string_dtype)
    assert np.isnan(ser.iloc[1])