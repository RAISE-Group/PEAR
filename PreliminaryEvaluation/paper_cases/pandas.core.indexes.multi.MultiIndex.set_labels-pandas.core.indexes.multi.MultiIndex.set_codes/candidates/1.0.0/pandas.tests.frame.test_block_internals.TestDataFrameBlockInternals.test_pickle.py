def test_pickle(self, float_string_frame, timezone_frame):
    empty_frame = DataFrame()
    unpickled = tm.round_trip_pickle(float_string_frame)
    tm.assert_frame_equal(float_string_frame, unpickled)
    float_string_frame._data.ndim
    unpickled = tm.round_trip_pickle(empty_frame)
    repr(unpickled)
    unpickled = tm.round_trip_pickle(timezone_frame)
    tm.assert_frame_equal(timezone_frame, unpickled)