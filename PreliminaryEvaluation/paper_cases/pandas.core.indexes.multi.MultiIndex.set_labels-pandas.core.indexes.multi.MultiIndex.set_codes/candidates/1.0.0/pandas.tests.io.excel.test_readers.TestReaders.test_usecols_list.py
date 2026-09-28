def test_usecols_list(self, read_ext, df_ref):
    if pd.read_excel.keywords['engine'] == 'pyxlsb':
        pytest.xfail('Sheets containing datetimes not supported by pyxlsb')
    df_ref = df_ref.reindex(columns=['B', 'C'])
    df1 = pd.read_excel('test1' + read_ext, 'Sheet1', index_col=0, usecols=[0, 2, 3])
    df2 = pd.read_excel('test1' + read_ext, 'Sheet2', skiprows=[1], index_col=0, usecols=[0, 2, 3])
    tm.assert_frame_equal(df1, df_ref, check_names=False)
    tm.assert_frame_equal(df2, df_ref, check_names=False)