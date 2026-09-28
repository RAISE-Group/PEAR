def test_header_and_index_with_types(self):
    df1 = self.read_html(self.spam_data, '.*Water.*', header=1, index_col=0)
    df2 = self.read_html(self.spam_data, 'Unit', header=1, index_col=0)
    assert_framelist_equal(df1, df2)