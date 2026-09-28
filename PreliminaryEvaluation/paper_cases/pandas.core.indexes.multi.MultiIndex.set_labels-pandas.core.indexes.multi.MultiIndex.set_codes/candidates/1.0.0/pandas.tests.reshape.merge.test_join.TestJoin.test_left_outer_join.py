def test_left_outer_join(self):
    joined_key2 = merge(self.df, self.df2, on='key2')
    _check_join(self.df, self.df2, joined_key2, ['key2'], how='left')
    joined_both = merge(self.df, self.df2)
    _check_join(self.df, self.df2, joined_both, ['key1', 'key2'], how='left')