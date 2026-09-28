def test_excelfile_fspath(self):
    with tm.ensure_clean('foo.xlsx') as path:
        df = DataFrame({'A': [1, 2]})
        df.to_excel(path)
        xl = ExcelFile(path)
        result = os.fspath(xl)
        assert result == path