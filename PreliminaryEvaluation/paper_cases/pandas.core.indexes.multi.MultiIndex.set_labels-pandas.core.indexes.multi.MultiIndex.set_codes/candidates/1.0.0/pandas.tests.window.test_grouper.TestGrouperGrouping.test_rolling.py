def test_rolling(self):
    g = self.frame.groupby('A')
    r = g.rolling(window=4)
    for f in ['sum', 'mean', 'min', 'max', 'count', 'kurt', 'skew']:
        result = getattr(r, f)()
        expected = g.apply(lambda x: getattr(x.rolling(4), f)())
        tm.assert_frame_equal(result, expected)
    for f in ['std', 'var']:
        result = getattr(r, f)(ddof=1)
        expected = g.apply(lambda x: getattr(x.rolling(4), f)(ddof=1))
        tm.assert_frame_equal(result, expected)