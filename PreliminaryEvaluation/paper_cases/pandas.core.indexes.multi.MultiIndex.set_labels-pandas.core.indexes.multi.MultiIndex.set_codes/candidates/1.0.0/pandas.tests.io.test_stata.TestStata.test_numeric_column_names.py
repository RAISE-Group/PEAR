def test_numeric_column_names(self):
    original = DataFrame(np.reshape(np.arange(25.0), (5, 5)))
    original.index.name = 'index'
    with tm.ensure_clean() as path:
        with tm.assert_produces_warning(InvalidColumnName):
            original.to_stata(path)
        written_and_read_again = self.read_dta(path)
        written_and_read_again = written_and_read_again.set_index('index')
        columns = list(written_and_read_again.columns)
        convert_col_name = lambda x: int(x[1])
        written_and_read_again.columns = map(convert_col_name, columns)
        tm.assert_frame_equal(original, written_and_read_again)