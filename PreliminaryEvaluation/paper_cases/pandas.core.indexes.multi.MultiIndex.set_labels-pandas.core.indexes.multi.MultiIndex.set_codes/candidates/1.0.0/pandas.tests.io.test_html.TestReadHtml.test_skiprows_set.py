def test_skiprows_set(self):
    df1 = self.read_html(self.spam_data, '.*Water.*', skiprows={1, 2})
    df2 = self.read_html(self.spam_data, 'Unit', skiprows={2, 1})
    assert_framelist_equal(df1, df2)