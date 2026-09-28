def test_reader_seconds(self, read_ext):
    if pd.read_excel.keywords['engine'] == 'pyxlsb':
        pytest.xfail('Sheets containing datetimes not supported by pyxlsb')
    expected = DataFrame.from_dict({'Time': [time(1, 2, 3), time(2, 45, 56, 100000), time(4, 29, 49, 200000), time(6, 13, 42, 300000), time(7, 57, 35, 400000), time(9, 41, 28, 500000), time(11, 25, 21, 600000), time(13, 9, 14, 700000), time(14, 53, 7, 800000), time(16, 37, 0, 900000), time(18, 20, 54)]})
    actual = pd.read_excel('times_1900' + read_ext, 'Sheet1')
    tm.assert_frame_equal(actual, expected)
    actual = pd.read_excel('times_1904' + read_ext, 'Sheet1')
    tm.assert_frame_equal(actual, expected)