def test_inner_join(self):
    joined_key2 = merge(self.df, self.df2, on='key2', how='inner')
    _check_join(self.df, self.df2, joined_key2, ['key2'], how='inner')
    joined_both = merge(self.df, self.df2, how='inner')
    _check_join(self.df, self.df2, joined_both, ['key1', 'key2'], how='inner')