def test_excelwriter_fspath(self):
    with tm.ensure_clean('foo.xlsx') as path:
        writer = ExcelWriter(path)
        assert os.fspath(writer) == str(path)