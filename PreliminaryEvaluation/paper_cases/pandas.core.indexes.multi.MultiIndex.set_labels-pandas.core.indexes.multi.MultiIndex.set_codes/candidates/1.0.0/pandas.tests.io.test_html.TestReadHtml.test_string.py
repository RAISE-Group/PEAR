def test_string(self):
    with open(self.spam_data, **self.spam_data_kwargs) as f:
        data = f.read()
    df1 = self.read_html(data, '.*Water.*')
    df2 = self.read_html(data, 'Unit')
    assert_framelist_equal(df1, df2)