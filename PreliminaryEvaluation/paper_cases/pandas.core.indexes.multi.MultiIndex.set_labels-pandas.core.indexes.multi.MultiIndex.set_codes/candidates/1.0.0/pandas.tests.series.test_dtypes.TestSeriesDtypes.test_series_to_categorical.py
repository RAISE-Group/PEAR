def test_series_to_categorical(self):
    series = Series(['a', 'b', 'c'])
    result = Series(series, dtype='category')
    expected = Series(['a', 'b', 'c'], dtype='category')
    tm.assert_series_equal(result, expected)