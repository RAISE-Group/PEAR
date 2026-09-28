def test_constructor_sequence(self):
    expected = Series(list(range(10)), dtype='int64')
    result = Series(range(10), dtype='int64')
    tm.assert_series_equal(result, expected)