def test_read_excel_skiprows_list(self, read_ext):
    if pd.read_excel.keywords['engine'] == 'pyxlsb':
        pytest.xfail('Sheets containing datetimes not supported by pyxlsb')
    actual = pd.read_excel('testskiprows' + read_ext, 'skiprows_list', skiprows=[0, 2])
    expected = DataFrame([[1, 2.5, pd.Timestamp('2015-01-01'), True], [2, 3.5, pd.Timestamp('2015-01-02'), False], [3, 4.5, pd.Timestamp('2015-01-03'), False], [4, 5.5, pd.Timestamp('2015-01-04'), True]], columns=['a', 'b', 'c', 'd'])
    tm.assert_frame_equal(actual, expected)
    actual = pd.read_excel('testskiprows' + read_ext, 'skiprows_list', skiprows=np.array([0, 2]))
    tm.assert_frame_equal(actual, expected)