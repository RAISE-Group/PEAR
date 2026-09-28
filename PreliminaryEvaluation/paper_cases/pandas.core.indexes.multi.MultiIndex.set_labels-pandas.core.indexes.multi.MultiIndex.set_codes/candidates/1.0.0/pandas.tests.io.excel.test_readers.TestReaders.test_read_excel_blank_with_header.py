def test_read_excel_blank_with_header(self, read_ext):
    expected = DataFrame(columns=['col_1', 'col_2'])
    actual = pd.read_excel('blank_with_header' + read_ext, 'Sheet1')
    tm.assert_frame_equal(actual, expected)