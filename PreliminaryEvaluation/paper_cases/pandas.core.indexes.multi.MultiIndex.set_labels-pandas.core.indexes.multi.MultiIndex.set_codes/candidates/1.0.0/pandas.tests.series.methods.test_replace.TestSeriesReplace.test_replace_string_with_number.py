def test_replace_string_with_number(self):
    s = pd.Series([1, 2, 3])
    result = s.replace('2', np.nan)
    expected = pd.Series([1, 2, 3])
    tm.assert_series_equal(expected, result)