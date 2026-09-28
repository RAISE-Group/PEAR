def test_file_like(self):
    with open(self.spam_data, **self.spam_data_kwargs) as f:
        df1 = self.read_html(f, '.*Water.*')
    with open(self.spam_data, **self.spam_data_kwargs) as f:
        df2 = self.read_html(f, 'Unit')
    assert_framelist_equal(df1, df2)