def test_rank_mixed_frame(self, float_string_frame):
    float_string_frame['datetime'] = datetime.now()
    float_string_frame['timedelta'] = timedelta(days=1, seconds=1)
    result = float_string_frame.rank(1)
    expected = float_string_frame.rank(1, numeric_only=True)
    tm.assert_frame_equal(result, expected)