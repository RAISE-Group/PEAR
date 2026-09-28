def test_conflicting_excel_engines(self, read_ext):
    msg = 'Engine should not be specified when passing an ExcelFile'
    with pd.ExcelFile('test1' + read_ext) as xl:
        with pytest.raises(ValueError, match=msg):
            pd.read_excel(xl, engine='foo')