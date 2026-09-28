def test_getitem(self):
    g = self.frame.groupby('A')
    g_mutated = get_groupby(self.frame, by='A', mutated=True)
    expected = g_mutated.B.apply(lambda x: x.rolling(2).mean())
    result = g.rolling(2).mean().B
    tm.assert_series_equal(result, expected)
    result = g.rolling(2).B.mean()
    tm.assert_series_equal(result, expected)
    result = g.B.rolling(2).mean()
    tm.assert_series_equal(result, expected)
    result = self.frame.B.groupby(self.frame.A).rolling(2).mean()
    tm.assert_series_equal(result, expected)