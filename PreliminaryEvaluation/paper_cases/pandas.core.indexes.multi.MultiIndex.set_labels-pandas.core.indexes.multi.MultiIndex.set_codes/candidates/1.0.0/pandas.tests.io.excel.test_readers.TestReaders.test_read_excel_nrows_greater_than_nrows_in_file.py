def test_read_excel_nrows_greater_than_nrows_in_file(self, read_ext):
    expected = pd.read_excel('test1' + read_ext)
    num_records_in_file = len(expected)
    num_rows_to_pull = num_records_in_file + 10
    actual = pd.read_excel('test1' + read_ext, nrows=num_rows_to_pull)
    tm.assert_frame_equal(actual, expected)