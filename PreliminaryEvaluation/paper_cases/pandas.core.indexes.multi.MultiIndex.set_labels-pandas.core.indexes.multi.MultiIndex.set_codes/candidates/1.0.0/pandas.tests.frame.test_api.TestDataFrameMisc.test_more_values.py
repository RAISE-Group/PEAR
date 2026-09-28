def test_more_values(self, float_string_frame):
    values = float_string_frame.values
    assert values.shape[1] == len(float_string_frame.columns)