def test_basic(self):
    frame = tm.makeTimeDataFrame()
    self._check_roundtrip(frame)