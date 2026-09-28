def test_single_variable(self):
    df = DataFrame(randn(10, 2))
    df2 = self.eval('df', local_dict={'df': df})
    tm.assert_frame_equal(df, df2)