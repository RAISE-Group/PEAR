def test_index(self):

    def _check(result, expected):
        if isinstance(result, Series):
            tm.assert_series_equal(result, expected)
        else:
            tm.assert_index_equal(result, expected)
    for klass in [Series, Index]:
        s = klass(['ABCDEFG', 'BCDEFEF', 'DEFGHIJEF', 'EFGHEF'])
        result = s.str.index('EF')
        _check(result, klass([4, 3, 1, 0]))
        expected = np.array([v.index('EF') for v in s.values], dtype=np.int64)
        tm.assert_numpy_array_equal(result.values, expected)
        result = s.str.rindex('EF')
        _check(result, klass([4, 5, 7, 4]))
        expected = np.array([v.rindex('EF') for v in s.values], dtype=np.int64)
        tm.assert_numpy_array_equal(result.values, expected)
        result = s.str.index('EF', 3)
        _check(result, klass([4, 3, 7, 4]))
        expected = np.array([v.index('EF', 3) for v in s.values], dtype=np.int64)
        tm.assert_numpy_array_equal(result.values, expected)
        result = s.str.rindex('EF', 3)
        _check(result, klass([4, 5, 7, 4]))
        expected = np.array([v.rindex('EF', 3) for v in s.values], dtype=np.int64)
        tm.assert_numpy_array_equal(result.values, expected)
        result = s.str.index('E', 4, 8)
        _check(result, klass([4, 5, 7, 4]))
        expected = np.array([v.index('E', 4, 8) for v in s.values], dtype=np.int64)
        tm.assert_numpy_array_equal(result.values, expected)
        result = s.str.rindex('E', 0, 5)
        _check(result, klass([4, 3, 1, 4]))
        expected = np.array([v.rindex('E', 0, 5) for v in s.values], dtype=np.int64)
        tm.assert_numpy_array_equal(result.values, expected)
        with pytest.raises(ValueError, match='substring not found'):
            result = s.str.index('DE')
        msg = 'expected a string object, not int'
        with pytest.raises(TypeError, match=msg):
            result = s.str.index(0)
    s = Series(['abcb', 'ab', 'bcbe', np.nan])
    result = s.str.index('b')
    tm.assert_series_equal(result, Series([1, 1, 0, np.nan]))
    result = s.str.rindex('b')
    tm.assert_series_equal(result, Series([3, 1, 2, np.nan]))