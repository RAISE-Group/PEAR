def test_from_records_empty(self):
    result = DataFrame.from_records([], columns=['a', 'b', 'c'])
    expected = DataFrame(columns=['a', 'b', 'c'])
    tm.assert_frame_equal(result, expected)
    result = DataFrame.from_records([], columns=['a', 'b', 'b'])
    expected = DataFrame(columns=['a', 'b', 'b'])
    tm.assert_frame_equal(result, expected)