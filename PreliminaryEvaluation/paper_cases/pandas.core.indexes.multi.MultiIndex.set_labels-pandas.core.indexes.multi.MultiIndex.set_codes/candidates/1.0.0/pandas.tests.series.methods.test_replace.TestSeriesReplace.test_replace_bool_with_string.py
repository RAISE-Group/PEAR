def test_replace_bool_with_string(self):
    s = pd.Series([True, False, True])
    result = s.replace(True, '2u')
    expected = pd.Series(['2u', False, '2u'])
    tm.assert_series_equal(expected, result)