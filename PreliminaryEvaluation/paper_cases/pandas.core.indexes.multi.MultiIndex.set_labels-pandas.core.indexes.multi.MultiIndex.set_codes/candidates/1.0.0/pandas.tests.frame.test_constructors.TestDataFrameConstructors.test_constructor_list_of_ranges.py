def test_constructor_list_of_ranges(self):
    result = DataFrame([range(10), range(10)])
    expected = DataFrame([list(range(10)), list(range(10))])
    tm.assert_frame_equal(result, expected)