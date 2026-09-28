def test_infer_types(self):
    df1 = self.read_html(self.spam_data, '.*Water.*', index_col=0)
    df2 = self.read_html(self.spam_data, 'Unit', index_col=0)
    assert_framelist_equal(df1, df2)