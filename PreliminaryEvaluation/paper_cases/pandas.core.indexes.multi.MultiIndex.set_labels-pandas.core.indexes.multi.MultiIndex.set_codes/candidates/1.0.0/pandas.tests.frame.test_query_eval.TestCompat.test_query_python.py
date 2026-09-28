def test_query_python(self):
    df = self.df
    result = df.query('A>0', engine='python')
    tm.assert_frame_equal(result, self.expected1)
    result = df.eval('A+1', engine='python')
    tm.assert_series_equal(result, self.expected2, check_names=False)