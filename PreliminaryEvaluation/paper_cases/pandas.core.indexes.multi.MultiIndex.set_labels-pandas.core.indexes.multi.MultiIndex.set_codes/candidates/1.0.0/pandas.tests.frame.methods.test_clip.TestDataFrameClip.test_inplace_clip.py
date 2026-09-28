def test_inplace_clip(self, float_frame):
    median = float_frame.median().median()
    frame_copy = float_frame.copy()
    frame_copy.clip(upper=median, lower=median, inplace=True)
    assert not (frame_copy.values != median).any()