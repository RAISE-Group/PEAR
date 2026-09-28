def test_skiprows_slice(self):
    df1 = self.read_html(self.spam_data, '.*Water.*', skiprows=1)
    df2 = self.read_html(self.spam_data, 'Unit', skiprows=1)
    assert_framelist_equal(df1, df2)