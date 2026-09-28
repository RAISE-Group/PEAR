def test_extractall_single_group_with_quantifier(self):
    s = Series(['ab3', 'abc3', 'd4cd2'], name='series_name')
    r = s.str.extractall('([a-z]+)')
    i = MultiIndex.from_tuples([(0, 0), (1, 0), (2, 0), (2, 1)], names=(None, 'match'))
    e = DataFrame(['ab', 'abc', 'd', 'cd'], i)
    tm.assert_frame_equal(r, e)