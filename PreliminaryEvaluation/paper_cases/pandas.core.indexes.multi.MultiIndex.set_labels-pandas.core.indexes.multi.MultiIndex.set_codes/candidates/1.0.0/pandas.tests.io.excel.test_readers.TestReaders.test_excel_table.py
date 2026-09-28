def test_excel_table(self, read_ext, df_ref):
    if pd.read_excel.keywords['engine'] == 'pyxlsb':
        pytest.xfail('Sheets containing datetimes not supported by pyxlsb')
    df1 = pd.read_excel('test1' + read_ext, 'Sheet1', index_col=0)
    df2 = pd.read_excel('test1' + read_ext, 'Sheet2', skiprows=[1], index_col=0)
    tm.assert_frame_equal(df1, df_ref, check_names=False)
    tm.assert_frame_equal(df2, df_ref, check_names=False)
    df3 = pd.read_excel('test1' + read_ext, 'Sheet1', index_col=0, skipfooter=1)
    tm.assert_frame_equal(df3, df1.iloc[:-1])