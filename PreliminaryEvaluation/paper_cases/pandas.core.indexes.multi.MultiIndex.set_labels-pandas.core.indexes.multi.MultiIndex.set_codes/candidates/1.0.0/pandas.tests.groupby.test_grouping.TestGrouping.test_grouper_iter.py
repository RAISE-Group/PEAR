def test_grouper_iter(self, df):
    assert sorted(df.groupby('A').grouper) == ['bar', 'foo']