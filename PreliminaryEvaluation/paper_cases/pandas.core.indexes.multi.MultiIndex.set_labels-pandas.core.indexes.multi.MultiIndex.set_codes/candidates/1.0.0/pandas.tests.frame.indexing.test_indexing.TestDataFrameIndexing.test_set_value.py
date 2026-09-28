def test_set_value(self, float_frame):
    for idx in float_frame.index:
        for col in float_frame.columns:
            float_frame._set_value(idx, col, 1)
            assert float_frame[col][idx] == 1