def test_handle_overlap(self):
    joined = merge(self.df, self.df2, on='key2', suffixes=['.foo', '.bar'])
    assert 'key1.foo' in joined
    assert 'key1.bar' in joined