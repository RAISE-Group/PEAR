def test_string_io(self):
    with open(self.spam_data, **self.spam_data_kwargs) as f:
        data1 = StringIO(f.read())
    with open(self.spam_data, **self.spam_data_kwargs) as f:
        data2 = StringIO(f.read())
    df1 = self.read_html(data1, '.*Water.*')
    df2 = self.read_html(data2, 'Unit')
    assert_framelist_equal(df1, df2)