def test_getitem_multiple(self):
    g = self.frame.groupby('A')
    r = g.rolling(2)
    g_mutated = get_groupby(self.frame, by='A', mutated=True)
    expected = g_mutated.B.apply(lambda x: x.rolling(2).count())
    result = r.B.count()
    tm.assert_series_equal(result, expected)
    result = r.B.count()
    tm.assert_series_equal(result, expected)