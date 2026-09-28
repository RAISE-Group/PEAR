def test_rolling_apply(self, raw):
    g = self.frame.groupby('A')
    r = g.rolling(window=4)
    result = r.apply(lambda x: x.sum(), raw=raw)
    expected = g.apply(lambda x: x.rolling(4).apply(lambda y: y.sum(), raw=raw))
    tm.assert_frame_equal(result, expected)