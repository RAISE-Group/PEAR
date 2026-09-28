def test_filter_corner(self):
    empty = DataFrame()
    result = empty.filter([])
    tm.assert_frame_equal(result, empty)
    result = empty.filter(like='foo')
    tm.assert_frame_equal(result, empty)