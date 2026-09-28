def test_excel_read_buffer(self, engine, read_ext):
    pth = 'test1' + read_ext
    expected = pd.read_excel(pth, 'Sheet1', index_col=0, engine=engine)
    with open(pth, 'rb') as f:
        with pd.ExcelFile(f) as xls:
            actual = pd.read_excel(xls, 'Sheet1', index_col=0)
    tm.assert_frame_equal(expected, actual)