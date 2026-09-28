def test_skiprows_ndarray(self):
    df1 = self.read_html(self.spam_data, '.*Water.*', skiprows=np.arange(2))
    df2 = self.read_html(self.spam_data, 'Unit', skiprows=np.arange(2))
    assert_framelist_equal(df1, df2)