def test_index_col_empty(self, read_ext):
    result = pd.read_excel('test1' + read_ext, 'Sheet3', index_col=['A', 'B', 'C'])
    expected = DataFrame(columns=['D', 'E', 'F'], index=MultiIndex(levels=[[]] * 3, codes=[[]] * 3, names=['A', 'B', 'C']))
    tm.assert_frame_equal(result, expected)