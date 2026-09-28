def test_invert(self, float_frame):
    df = float_frame
    tm.assert_frame_equal(-(df < 0), ~(df < 0))