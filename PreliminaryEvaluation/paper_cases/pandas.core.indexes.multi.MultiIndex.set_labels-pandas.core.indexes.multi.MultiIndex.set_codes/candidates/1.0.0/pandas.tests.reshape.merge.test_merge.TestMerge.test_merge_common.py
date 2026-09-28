def test_merge_common(self):
    joined = merge(self.df, self.df2)
    exp = merge(self.df, self.df2, on=['key1', 'key2'])
    tm.assert_frame_equal(joined, exp)