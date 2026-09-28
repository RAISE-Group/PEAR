def test_date_conversion_overflow(self, read_ext):
    if pd.read_excel.keywords['engine'] == 'pyxlsb':
        pytest.xfail('Sheets containing datetimes not supported by pyxlsb')
    expected = pd.DataFrame([[pd.Timestamp('2016-03-12'), 'Marc Johnson'], [pd.Timestamp('2016-03-16'), 'Jack Black'], [1e+20, 'Timothy Brown']], columns=['DateColWithBigInt', 'StringCol'])
    if pd.read_excel.keywords['engine'] == 'openpyxl':
        pytest.xfail('Maybe not supported by openpyxl')
    result = pd.read_excel('testdateoverflow' + read_ext)
    tm.assert_frame_equal(result, expected)