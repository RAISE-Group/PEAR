def test_read_excel_squeeze(self, read_ext):
    f = 'test_squeeze' + read_ext
    actual = pd.read_excel(f, 'two_columns', index_col=0, squeeze=True)
    expected = pd.Series([2, 3, 4], [4, 5, 6], name='b')
    expected.index.name = 'a'
    tm.assert_series_equal(actual, expected)
    actual = pd.read_excel(f, 'two_columns', squeeze=True)
    expected = pd.DataFrame({'a': [4, 5, 6], 'b': [2, 3, 4]})
    tm.assert_frame_equal(actual, expected)
    actual = pd.read_excel(f, 'one_column', squeeze=True)
    expected = pd.Series([1, 2, 3], name='a')
    tm.assert_series_equal(actual, expected)