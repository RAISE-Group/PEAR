def test_compare_to_int(self, any_nullable_int_dtype, all_compare_operators):
    s1 = pd.Series([1, None, 3], dtype=any_nullable_int_dtype)
    s2 = pd.Series([1, None, 3], dtype='float')
    method = getattr(s1, all_compare_operators)
    result = method(2)
    method = getattr(s2, all_compare_operators)
    expected = method(2).astype('boolean')
    expected[s2.isna()] = pd.NA
    self.assert_series_equal(result, expected)