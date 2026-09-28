def test_all(self):
    df = self.regular * 2
    er = df.rolling(window=1)
    r = df.rolling(window='1s')
    for f in ['sum', 'mean', 'count', 'median', 'std', 'var', 'kurt', 'skew', 'min', 'max']:
        result = getattr(r, f)()
        expected = getattr(er, f)()
        tm.assert_frame_equal(result, expected)
    result = r.quantile(0.5)
    expected = er.quantile(0.5)
    tm.assert_frame_equal(result, expected)