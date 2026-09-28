def test_constructor_single_str(self):
    expected = Series(['abc'])
    result = Series('abc')
    tm.assert_series_equal(result, expected)