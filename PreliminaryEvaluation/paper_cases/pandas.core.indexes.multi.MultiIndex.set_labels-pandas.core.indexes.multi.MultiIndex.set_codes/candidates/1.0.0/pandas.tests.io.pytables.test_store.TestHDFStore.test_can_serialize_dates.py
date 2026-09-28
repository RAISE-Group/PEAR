def test_can_serialize_dates(self, setup_path):
    rng = [x.date() for x in bdate_range('1/1/2000', '1/30/2000')]
    frame = DataFrame(np.random.randn(len(rng), 4), index=rng)
    self._check_roundtrip(frame, tm.assert_frame_equal, path=setup_path)