def test_transpose_get_view(self, float_frame):
    dft = float_frame.T
    dft.values[:, 5:10] = 5
    assert (float_frame.values[5:10] == 5).all()