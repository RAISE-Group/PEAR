def test_sheet_name(self, read_ext, df_ref):
    if pd.read_excel.keywords['engine'] == 'pyxlsb':
        pytest.xfail('Sheets containing datetimes not supported by pyxlsb')
    filename = 'test1'
    sheet_name = 'Sheet1'
    if pd.read_excel.keywords['engine'] == 'openpyxl':
        pytest.xfail('Maybe not supported by openpyxl')
    df1 = pd.read_excel(filename + read_ext, sheet_name=sheet_name, index_col=0)
    with ignore_xlrd_time_clock_warning():
        df2 = pd.read_excel(filename + read_ext, index_col=0, sheet_name=sheet_name)
    tm.assert_frame_equal(df1, df_ref, check_names=False)
    tm.assert_frame_equal(df2, df_ref, check_names=False)