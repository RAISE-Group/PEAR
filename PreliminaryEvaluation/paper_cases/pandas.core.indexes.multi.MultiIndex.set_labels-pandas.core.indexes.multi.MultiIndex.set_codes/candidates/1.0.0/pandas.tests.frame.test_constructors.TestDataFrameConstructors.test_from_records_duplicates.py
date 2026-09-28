def test_from_records_duplicates(self):
    result = DataFrame.from_records([(1, 2, 3), (4, 5, 6)], columns=['a', 'b', 'a'])
    expected = DataFrame([(1, 2, 3), (4, 5, 6)], columns=['a', 'b', 'a'])
    tm.assert_frame_equal(result, expected)