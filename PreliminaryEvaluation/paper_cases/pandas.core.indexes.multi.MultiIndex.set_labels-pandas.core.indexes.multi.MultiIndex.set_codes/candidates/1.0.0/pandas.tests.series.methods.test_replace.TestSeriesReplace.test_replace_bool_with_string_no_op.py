def test_replace_bool_with_string_no_op(self):
    s = pd.Series([True, False, True])
    result = s.replace('fun', 'in-the-sun')
    tm.assert_series_equal(s, result)