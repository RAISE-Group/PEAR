def test_extractall_stringindex(self):
    s = Series(['a1a2', 'b1', 'c1'], name='xxx')
    res = s.str.extractall('[ab](?P<digit>\\d)')
    exp_idx = MultiIndex.from_tuples([(0, 0), (0, 1), (1, 0)], names=[None, 'match'])
    exp = DataFrame({'digit': ['1', '2', '1']}, index=exp_idx)
    tm.assert_frame_equal(res, exp)
    for idx in [Index(['a1a2', 'b1', 'c1']), Index(['a1a2', 'b1', 'c1'], name='xxx')]:
        res = idx.str.extractall('[ab](?P<digit>\\d)')
        tm.assert_frame_equal(res, exp)
    s = Series(['a1a2', 'b1', 'c1'], name='s_name', index=Index(['XX', 'yy', 'zz'], name='idx_name'))
    res = s.str.extractall('[ab](?P<digit>\\d)')
    exp_idx = MultiIndex.from_tuples([('XX', 0), ('XX', 1), ('yy', 0)], names=['idx_name', 'match'])
    exp = DataFrame({'digit': ['1', '2', '1']}, index=exp_idx)
    tm.assert_frame_equal(res, exp)