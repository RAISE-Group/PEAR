def test_expanding_apply(self, raw):
    g = self.frame.groupby('A')
    r = g.expanding()
    result = r.apply(lambda x: x.sum(), raw=raw)
    expected = g.apply(lambda x: x.expanding().apply(lambda y: y.sum(), raw=raw))
    tm.assert_frame_equal(result, expected)