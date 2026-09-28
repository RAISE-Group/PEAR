def test_extractall_single_group(self):
    s = Series(['a3', 'b3', 'd4c2'], name='series_name')
    r = s.str.extractall('(?P<letter>[a-z])')
    i = MultiIndex.from_tuples([(0, 0), (1, 0), (2, 0), (2, 1)], names=(None, 'match'))
    e = DataFrame({'letter': ['a', 'b', 'd', 'c']}, i)
    tm.assert_frame_equal(r, e)
    r = s.str.extractall('([a-z])')
    e = DataFrame(['a', 'b', 'd', 'c'], i)
    tm.assert_frame_equal(r, e)