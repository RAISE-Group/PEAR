def test_transpose(self, timezone_frame):
    result = timezone_frame.T
    expected = DataFrame(timezone_frame.values.T)
    expected.index = ['A', 'B', 'C']
    tm.assert_frame_equal(result, expected)