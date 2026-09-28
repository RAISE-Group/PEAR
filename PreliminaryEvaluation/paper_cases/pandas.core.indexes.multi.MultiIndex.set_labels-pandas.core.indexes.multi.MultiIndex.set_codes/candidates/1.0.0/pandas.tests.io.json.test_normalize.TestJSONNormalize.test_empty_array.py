def test_empty_array(self):
    result = json_normalize([])
    expected = DataFrame()
    tm.assert_frame_equal(result, expected)