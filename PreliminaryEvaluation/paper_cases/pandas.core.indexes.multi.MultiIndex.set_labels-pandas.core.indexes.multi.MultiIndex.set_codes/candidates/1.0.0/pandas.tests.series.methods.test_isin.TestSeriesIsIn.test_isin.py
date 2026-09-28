def test_isin(self):
    s = Series(['A', 'B', 'C', 'a', 'B', 'B', 'A', 'C'])
    result = s.isin(['A', 'C'])
    expected = Series([True, False, True, False, False, False, True, True])
    tm.assert_series_equal(result, expected)
    s = Series(list('abcdefghijk' * 10 ** 5))
    in_list = [-1, 'a', 'b', 'G', 'Y', 'Z', 'E', 'K', 'E', 'S', 'I', 'R', 'R'] * 6
    assert s.isin(in_list).sum() == 200000