def test_excel_stop_iterator(self, read_ext):
    parsed = pd.read_excel('test2' + read_ext, 'Sheet1')
    expected = DataFrame([['aaaa', 'bbbbb']], columns=['Test', 'Test1'])
    tm.assert_frame_equal(parsed, expected)