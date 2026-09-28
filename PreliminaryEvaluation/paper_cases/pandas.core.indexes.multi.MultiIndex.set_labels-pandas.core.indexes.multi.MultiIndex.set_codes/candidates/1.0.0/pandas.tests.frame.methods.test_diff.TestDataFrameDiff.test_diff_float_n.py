def test_diff_float_n(self, datetime_frame):
    rs = datetime_frame.diff(1.0)
    xp = datetime_frame.diff(1)
    tm.assert_frame_equal(rs, xp)