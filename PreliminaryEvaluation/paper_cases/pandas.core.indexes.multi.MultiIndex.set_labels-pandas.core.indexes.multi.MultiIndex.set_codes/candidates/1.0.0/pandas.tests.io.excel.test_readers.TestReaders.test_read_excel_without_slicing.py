def test_read_excel_without_slicing(self, read_ext, df_ref):
    if pd.read_excel.keywords['engine'] == 'pyxlsb':
        pytest.xfail('Sheets containing datetimes not supported by pyxlsb')
    expected = df_ref
    result = pd.read_excel('test1' + read_ext, 'Sheet1', index_col=0)
    tm.assert_frame_equal(result, expected, check_names=False)