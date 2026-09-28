def test_spam(self):
    df1 = self.read_html(self.spam_data, '.*Water.*')
    df2 = self.read_html(self.spam_data, 'Unit')
    assert_framelist_equal(df1, df2)
    assert df1[0].iloc[0, 0] == 'Proximates'
    assert df1[0].columns[0] == 'Nutrient'