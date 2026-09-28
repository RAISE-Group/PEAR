def test_transpose(self, uint64_frame):
    result = uint64_frame.T
    expected = DataFrame(uint64_frame.values.T)
    expected.index = ['A', 'B']
    tm.assert_frame_equal(result, expected)