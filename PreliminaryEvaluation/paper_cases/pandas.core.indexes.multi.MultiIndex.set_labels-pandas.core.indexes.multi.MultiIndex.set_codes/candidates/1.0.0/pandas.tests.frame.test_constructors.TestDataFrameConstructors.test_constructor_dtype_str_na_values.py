def test_constructor_dtype_str_na_values(self, string_dtype):
    df = DataFrame({'A': ['x', None]}, dtype=string_dtype)
    result = df.isna()
    expected = DataFrame({'A': [False, True]})
    tm.assert_frame_equal(result, expected)
    assert df.iloc[1, 0] is None
    df = DataFrame({'A': ['x', np.nan]}, dtype=string_dtype)
    assert np.isnan(df.iloc[1, 0])