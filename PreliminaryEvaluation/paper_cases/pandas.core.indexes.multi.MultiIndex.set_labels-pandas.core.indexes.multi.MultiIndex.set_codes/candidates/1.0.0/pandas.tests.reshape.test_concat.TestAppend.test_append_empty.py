def test_append_empty(self, float_frame):
    empty = DataFrame()
    appended = float_frame.append(empty)
    tm.assert_frame_equal(float_frame, appended)
    assert appended is not float_frame
    appended = empty.append(float_frame)
    tm.assert_frame_equal(float_frame, appended)
    assert appended is not float_frame