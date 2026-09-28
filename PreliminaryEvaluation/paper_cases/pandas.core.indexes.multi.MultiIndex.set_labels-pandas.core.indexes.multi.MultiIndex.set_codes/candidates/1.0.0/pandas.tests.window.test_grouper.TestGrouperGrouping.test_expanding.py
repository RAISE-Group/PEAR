def test_expanding(self):
    g = self.frame.groupby('A')
    r = g.expanding()
    for f in ['sum', 'mean', 'min', 'max', 'count', 'kurt', 'skew']:
        result = getattr(r, f)()
        expected = g.apply(lambda x: getattr(x.expanding(), f)())
        tm.assert_frame_equal(result, expected)
    for f in ['std', 'var']:
        result = getattr(r, f)(ddof=0)
        expected = g.apply(lambda x: getattr(x.expanding(), f)(ddof=0))
        tm.assert_frame_equal(result, expected)