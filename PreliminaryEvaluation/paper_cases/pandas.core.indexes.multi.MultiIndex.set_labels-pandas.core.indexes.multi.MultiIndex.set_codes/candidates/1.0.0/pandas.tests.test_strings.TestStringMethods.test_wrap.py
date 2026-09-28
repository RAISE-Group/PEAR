def test_wrap(self):
    values = Series(['hello world', 'hello world!', 'hello world!!', 'abcdefabcde', 'abcdefabcdef', 'abcdefabcdefa', 'ab ab ab ab ', 'ab ab ab ab a', '\t'])
    xp = Series(['hello world', 'hello world!', 'hello\nworld!!', 'abcdefabcde', 'abcdefabcdef', 'abcdefabcdef\na', 'ab ab ab ab', 'ab ab ab ab\na', ''])
    rs = values.str.wrap(12, break_long_words=True)
    tm.assert_series_equal(rs, xp)
    values = Series(['  pre  ', np.nan, '¬€耀 abadcafe'])
    xp = Series(['  pre', np.nan, '¬€耀 ab\nadcafe'])
    rs = values.str.wrap(6)
    tm.assert_series_equal(rs, xp)