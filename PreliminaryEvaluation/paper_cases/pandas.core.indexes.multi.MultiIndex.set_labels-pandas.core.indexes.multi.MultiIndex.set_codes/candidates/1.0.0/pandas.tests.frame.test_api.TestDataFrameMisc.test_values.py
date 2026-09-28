def test_values(self, float_frame):
    float_frame.values[:, 0] = 5.0
    assert (float_frame.values[:, 0] == 5).all()