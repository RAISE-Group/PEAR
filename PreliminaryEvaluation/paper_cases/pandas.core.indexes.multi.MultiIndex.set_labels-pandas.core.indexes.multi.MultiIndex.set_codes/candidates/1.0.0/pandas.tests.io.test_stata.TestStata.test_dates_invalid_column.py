def test_dates_invalid_column(self):
    original = DataFrame([datetime(2006, 11, 19, 23, 13, 20)])
    original.index.name = 'index'
    with tm.ensure_clean() as path:
        with tm.assert_produces_warning(InvalidColumnName):
            original.to_stata(path, {0: 'tc'})
        written_and_read_again = self.read_dta(path)
        modified = original.copy()
        modified.columns = ['_0']
        tm.assert_frame_equal(written_and_read_again.set_index('index'), modified)