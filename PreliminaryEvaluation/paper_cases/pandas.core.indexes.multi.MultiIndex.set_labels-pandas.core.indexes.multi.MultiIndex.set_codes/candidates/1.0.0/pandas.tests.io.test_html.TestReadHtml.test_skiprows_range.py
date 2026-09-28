def test_skiprows_range(self):
    df1 = self.read_html(self.spam_data, '.*Water.*', skiprows=range(2))[0]
    df2 = self.read_html(self.spam_data, 'Unit', skiprows=range(2))[0]
    tm.assert_frame_equal(df1, df2)