@pytest.mark.parametrize('index_col', [None, 2])
def test_index_col_with_unnamed(self, read_ext, index_col):
    result = pd.read_excel('test1' + read_ext, 'Sheet4', index_col=index_col)
    expected = DataFrame([['i1', 'a', 'x'], ['i2', 'b', 'y']], columns=['Unnamed: 0', 'col1', 'col2'])
    if index_col:
        expected = expected.set_index(expected.columns[index_col])
    tm.assert_frame_equal(result, expected)