@pytest.mark.parametrize('usecols', [[0, 1, 3], [0, 3, 1], [1, 0, 3], [1, 3, 0], [3, 0, 1], [3, 1, 0]])
def test_usecols_diff_positional_int_columns_order(self, read_ext, usecols, df_ref):
    if pd.read_excel.keywords['engine'] == 'pyxlsb':
        pytest.xfail('Sheets containing datetimes not supported by pyxlsb')
    expected = df_ref[['A', 'C']]
    result = pd.read_excel('test1' + read_ext, 'Sheet1', index_col=0, usecols=usecols)
    tm.assert_frame_equal(result, expected, check_names=False)