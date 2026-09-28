def test_read_excel_nrows(self, read_ext):
    num_rows_to_pull = 5
    actual = pd.read_excel('test1' + read_ext, nrows=num_rows_to_pull)
    expected = pd.read_excel('test1' + read_ext)
    expected = expected[:num_rows_to_pull]
    tm.assert_frame_equal(actual, expected)