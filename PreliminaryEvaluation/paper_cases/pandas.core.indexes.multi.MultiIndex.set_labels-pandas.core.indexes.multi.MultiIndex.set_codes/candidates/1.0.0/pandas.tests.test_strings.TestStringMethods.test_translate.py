def test_translate(self):

    def _check(result, expected):
        if isinstance(result, Series):
            tm.assert_series_equal(result, expected)
        else:
            tm.assert_index_equal(result, expected)
    for klass in [Series, Index]:
        s = klass(['abcdefg', 'abcc', 'cdddfg', 'cdefggg'])
        table = str.maketrans('abc', 'cde')
        result = s.str.translate(table)
        expected = klass(['cdedefg', 'cdee', 'edddfg', 'edefggg'])
        _check(result, expected)
    s = Series(['a', 'b', 'c', 1.2])
    expected = Series(['c', 'd', 'e', np.nan])
    result = s.str.translate(table)
    tm.assert_series_equal(result, expected)