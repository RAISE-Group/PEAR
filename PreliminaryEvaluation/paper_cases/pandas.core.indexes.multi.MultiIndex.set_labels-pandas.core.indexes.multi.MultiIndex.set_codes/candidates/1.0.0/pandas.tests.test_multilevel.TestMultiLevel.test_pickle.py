def test_pickle(self):

    def _test_roundtrip(frame):
        unpickled = tm.round_trip_pickle(frame)
        tm.assert_frame_equal(frame, unpickled)
    _test_roundtrip(self.frame)
    _test_roundtrip(self.frame.T)
    _test_roundtrip(self.ymd)
    _test_roundtrip(self.ymd.T)