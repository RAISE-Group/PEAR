def test_iter(self, float_frame):
    assert tm.equalContents(list(float_frame), float_frame.columns)