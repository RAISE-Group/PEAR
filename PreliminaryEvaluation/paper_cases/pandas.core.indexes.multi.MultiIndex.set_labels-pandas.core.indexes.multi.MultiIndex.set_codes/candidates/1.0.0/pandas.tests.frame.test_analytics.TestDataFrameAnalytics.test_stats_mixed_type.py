def test_stats_mixed_type(self, float_string_frame):
    float_string_frame.std(1)
    float_string_frame.var(1)
    float_string_frame.mean(1)
    float_string_frame.skew(1)