def test_pipe_failures(self):
    s = Series(['A|B|C'])
    result = s.str.split('|')
    exp = Series([['A', 'B', 'C']])
    tm.assert_series_equal(result, exp)
    result = s.str.replace('|', ' ')
    exp = Series(['A B C'])
    tm.assert_series_equal(result, exp)