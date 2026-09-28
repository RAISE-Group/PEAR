def test_reader_closes_file(self, engine, read_ext):
    f = open('test1' + read_ext, 'rb')
    with pd.ExcelFile(f) as xlsx:
        pd.read_excel(xlsx, 'Sheet1', index_col=0, engine=engine)
    assert f.closed