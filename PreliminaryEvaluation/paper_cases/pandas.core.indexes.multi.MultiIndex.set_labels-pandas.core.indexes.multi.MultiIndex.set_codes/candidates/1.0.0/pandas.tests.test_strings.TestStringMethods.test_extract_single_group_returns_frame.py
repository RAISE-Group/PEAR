def test_extract_single_group_returns_frame(self):
    s = Series(['a3', 'b3', 'c2'], name='series_name')
    r = s.str.extract('(?P<letter>[a-z])', expand=True)
    e = DataFrame({'letter': ['a', 'b', 'c']})
    tm.assert_frame_equal(r, e)