def test_excel_table_sheet_by_index(self, read_ext, df_ref):
    if read_ext == '.xlsb':
        pytest.xfail('Sheets containing datetimes not supported by pyxlsb')
    with pd.ExcelFile('test1' + read_ext) as excel:
        df1 = pd.read_excel(excel, 0, index_col=0)
        df2 = pd.read_excel(excel, 1, skiprows=[1], index_col=0)
    tm.assert_frame_equal(df1, df_ref, check_names=False)
    tm.assert_frame_equal(df2, df_ref, check_names=False)
    with pd.ExcelFile('test1' + read_ext) as excel:
        df1 = excel.parse(0, index_col=0)
        df2 = excel.parse(1, skiprows=[1], index_col=0)
    tm.assert_frame_equal(df1, df_ref, check_names=False)
    tm.assert_frame_equal(df2, df_ref, check_names=False)
    with pd.ExcelFile('test1' + read_ext) as excel:
        df3 = pd.read_excel(excel, 0, index_col=0, skipfooter=1)
    tm.assert_frame_equal(df3, df1.iloc[:-1])
    with pd.ExcelFile('test1' + read_ext) as excel:
        df3 = excel.parse(0, index_col=0, skipfooter=1)
    tm.assert_frame_equal(df3, df1.iloc[:-1])