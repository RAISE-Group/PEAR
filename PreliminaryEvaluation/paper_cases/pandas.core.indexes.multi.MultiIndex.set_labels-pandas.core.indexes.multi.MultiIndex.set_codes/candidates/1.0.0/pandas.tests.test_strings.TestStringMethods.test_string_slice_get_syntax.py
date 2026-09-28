def test_string_slice_get_syntax(self):
    s = Series(['YYY', 'B', 'C', 'YYYYYYbYYY', 'BYYYcYYY', np.nan, 'CYYYBYYY', 'dog', 'cYYYt'])
    result = s.str[0]
    expected = s.str.get(0)
    tm.assert_series_equal(result, expected)
    result = s.str[:3]
    expected = s.str.slice(stop=3)
    tm.assert_series_equal(result, expected)
    result = s.str[2::-1]
    expected = s.str.slice(start=2, step=-1)
    tm.assert_series_equal(result, expected)