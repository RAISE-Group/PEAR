def test_string_slice_out_of_bounds(self):
    s = Series([(1, 2), (1,), (3, 4, 5)])
    result = s.str[1]
    expected = Series([2, np.nan, 4])
    tm.assert_series_equal(result, expected)
    s = Series(['foo', 'b', 'ba'])
    result = s.str[1]
    expected = Series(['o', np.nan, 'a'])
    tm.assert_series_equal(result, expected)