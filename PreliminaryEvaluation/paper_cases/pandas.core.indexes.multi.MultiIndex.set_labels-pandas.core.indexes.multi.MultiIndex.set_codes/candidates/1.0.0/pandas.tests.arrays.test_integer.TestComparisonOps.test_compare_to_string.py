def test_compare_to_string(self, any_nullable_int_dtype):
    s = pd.Series([1, None], dtype=any_nullable_int_dtype)
    result = s == 'a'
    expected = pd.Series([False, pd.NA], dtype='boolean')
    self.assert_series_equal(result, expected)