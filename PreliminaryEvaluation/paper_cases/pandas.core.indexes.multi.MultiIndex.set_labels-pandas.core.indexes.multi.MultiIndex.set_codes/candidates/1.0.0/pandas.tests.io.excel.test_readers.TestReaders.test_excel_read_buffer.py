def test_excel_read_buffer(self, read_ext):
    pth = 'test1' + read_ext
    expected = pd.read_excel(pth, 'Sheet1', index_col=0)
    with open(pth, 'rb') as f:
        actual = pd.read_excel(f, 'Sheet1', index_col=0)
        tm.assert_frame_equal(expected, actual)