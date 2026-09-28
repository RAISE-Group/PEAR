def test_merge_index_as_on_arg(self):
    left = self.df.set_index('key1')
    right = self.df2.set_index('key1')
    result = merge(left, right, on='key1')
    expected = merge(self.df, self.df2, on='key1').set_index('key1')
    tm.assert_frame_equal(result, expected)