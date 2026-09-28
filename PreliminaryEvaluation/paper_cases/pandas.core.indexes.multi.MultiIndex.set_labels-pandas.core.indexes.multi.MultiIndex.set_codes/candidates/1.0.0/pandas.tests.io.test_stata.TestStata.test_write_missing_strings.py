def test_write_missing_strings(self):
    original = DataFrame([['1'], [None]], columns=['foo'])
    expected = DataFrame([['1'], ['']], columns=['foo'])
    expected.index.name = 'index'
    with tm.ensure_clean() as path:
        original.to_stata(path)
        written_and_read_again = self.read_dta(path)
        tm.assert_frame_equal(written_and_read_again.set_index('index'), expected)