@pytest.mark.parametrize('usecols', [['B', 'D'], ['D', 'B']])
def test_usecols_diff_positional_str_columns_order(self, read_ext, usecols, df_ref):
    expected = df_ref[['B', 'D']]
    expected.index = range(len(expected))
    result = pd.read_excel('test1' + read_ext, 'Sheet1', usecols=usecols)
    tm.assert_frame_equal(result, expected, check_names=False)