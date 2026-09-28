def test_clip(self, float_frame):
    median = float_frame.median().median()
    original = float_frame.copy()
    double = float_frame.clip(upper=median, lower=median)
    assert not (double.values != median).any()
    assert (float_frame.values == original.values).all()