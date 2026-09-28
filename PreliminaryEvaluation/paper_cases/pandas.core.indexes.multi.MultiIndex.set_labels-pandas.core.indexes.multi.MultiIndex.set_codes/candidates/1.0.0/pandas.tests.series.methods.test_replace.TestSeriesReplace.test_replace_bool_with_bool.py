def test_replace_bool_with_bool(self):
    s = pd.Series([True, False, True])
    result = s.replace(True, False)
    expected = pd.Series([False] * len(s))
    tm.assert_series_equal(expected, result)