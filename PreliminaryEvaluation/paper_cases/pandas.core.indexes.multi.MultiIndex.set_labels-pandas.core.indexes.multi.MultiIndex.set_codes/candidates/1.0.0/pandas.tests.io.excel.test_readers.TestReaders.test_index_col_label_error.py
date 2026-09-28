def test_index_col_label_error(self, read_ext):
    msg = 'list indices must be integers.*, not str'
    with pytest.raises(TypeError, match=msg):
        pd.read_excel('test1' + read_ext, 'Sheet1', index_col=['A'], usecols=['A', 'C'])