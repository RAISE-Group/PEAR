def test_get_complex(self):
    values = Series([(1, 2, 3), [1, 2, 3], {1, 2, 3}, {1: 'a', 2: 'b', 3: 'c'}])
    result = values.str.get(1)
    expected = Series([2, 2, np.nan, 'a'])
    tm.assert_series_equal(result, expected)
    result = values.str.get(-1)
    expected = Series([3, 3, np.nan, np.nan])
    tm.assert_series_equal(result, expected)