def test_handle_overlap_arbitrary_key(self):
    joined = merge(self.df, self.df2, left_on='key2', right_on='key1', suffixes=['.foo', '.bar'])
    assert 'key1.foo' in joined
    assert 'key2.bar' in joined