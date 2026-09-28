def test_read_excel_blank(self, read_ext):
    actual = pd.read_excel('blank' + read_ext, 'Sheet1')
    tm.assert_frame_equal(actual, DataFrame())