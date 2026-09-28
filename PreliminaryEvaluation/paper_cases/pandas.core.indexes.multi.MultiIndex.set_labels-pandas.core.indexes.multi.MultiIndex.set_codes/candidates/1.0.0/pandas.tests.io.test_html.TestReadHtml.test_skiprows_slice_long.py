def test_skiprows_slice_long(self):
    df1 = self.read_html(self.spam_data, '.*Water.*', skiprows=slice(2, 5))
    df2 = self.read_html(self.spam_data, 'Unit', skiprows=slice(4, 1, -1))
    assert_framelist_equal(df1, df2)