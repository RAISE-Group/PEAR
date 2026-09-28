def test_usecols_excel_range_str(self, read_ext, df_ref):
    if pd.read_excel.keywords['engine'] == 'pyxlsb':
        pytest.xfail('Sheets containing datetimes not supported by pyxlsb')
    expected = df_ref[['C', 'D']]
    result = pd.read_excel('test1' + read_ext, 'Sheet1', index_col=0, usecols='A,D:E')
    tm.assert_frame_equal(result, expected, check_names=False)