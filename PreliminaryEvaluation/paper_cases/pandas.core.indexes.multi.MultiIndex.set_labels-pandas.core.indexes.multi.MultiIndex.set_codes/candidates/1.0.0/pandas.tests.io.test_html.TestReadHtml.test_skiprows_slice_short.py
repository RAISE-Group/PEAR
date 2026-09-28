def test_skiprows_slice_short(self):
    df1 = self.read_html(self.spam_data, '.*Water.*', skiprows=slice(2))
    df2 = self.read_html(self.spam_data, 'Unit', skiprows=slice(2))
    assert_framelist_equal(df1, df2)