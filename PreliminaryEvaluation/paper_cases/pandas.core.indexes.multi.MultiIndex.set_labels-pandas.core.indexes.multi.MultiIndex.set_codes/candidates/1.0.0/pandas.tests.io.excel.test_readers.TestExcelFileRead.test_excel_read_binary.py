def test_excel_read_binary(self, engine, read_ext):
    expected = pd.read_excel('test1' + read_ext, engine=engine)
    with open('test1' + read_ext, 'rb') as f:
        data = f.read()
    actual = pd.read_excel(data, engine=engine)
    tm.assert_frame_equal(expected, actual)