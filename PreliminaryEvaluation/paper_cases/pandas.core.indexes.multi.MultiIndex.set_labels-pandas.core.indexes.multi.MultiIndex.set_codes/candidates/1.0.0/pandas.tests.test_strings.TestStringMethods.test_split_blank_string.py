def test_split_blank_string(self):
    values = Series([''], name='test')
    result = values.str.split(expand=True)
    exp = DataFrame([[]])
    tm.assert_frame_equal(result, exp)
    values = Series(['a b c', 'a b', '', ' '], name='test')
    result = values.str.split(expand=True)
    exp = DataFrame([['a', 'b', 'c'], ['a', 'b', np.nan], [np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan]])
    tm.assert_frame_equal(result, exp)