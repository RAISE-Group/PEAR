def test_excel_cell_error_na(self, read_ext):
    if pd.read_excel.keywords['engine'] == 'pyxlsb':
        pytest.xfail('Sheets containing datetimes not supported by pyxlsb')
    parsed = pd.read_excel('test3' + read_ext, 'Sheet1')
    expected = DataFrame([[np.nan]], columns=['Test'])
    tm.assert_frame_equal(parsed, expected)