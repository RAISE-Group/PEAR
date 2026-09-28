def test_len(self, float_frame):
    assert len(float_frame) == len(float_frame.index)