def test_read_write_dta5(self):
    original = DataFrame([(np.nan, np.nan, np.nan, np.nan, np.nan)], columns=['float_miss', 'double_miss', 'byte_miss', 'int_miss', 'long_miss'])
    original.index.name = 'index'
    with tm.ensure_clean() as path:
        original.to_stata(path, None)
        written_and_read_again = self.read_dta(path)
        tm.assert_frame_equal(written_and_read_again.set_index('index'), original)