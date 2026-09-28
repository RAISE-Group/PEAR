def test_sheet_name(self, read_ext, df_ref):
    if read_ext == '.xlsb':
        pytest.xfail('Sheets containing datetimes not supported by pyxlsb')
    filename = 'test1'
    sheet_name = 'Sheet1'
    with pd.ExcelFile(filename + read_ext) as excel:
        df1_parse = excel.parse(sheet_name=sheet_name, index_col=0)
    with pd.ExcelFile(filename + read_ext) as excel:
        df2_parse = excel.parse(index_col=0, sheet_name=sheet_name)
    tm.assert_frame_equal(df1_parse, df_ref, check_names=False)
    tm.assert_frame_equal(df2_parse, df_ref, check_names=False)