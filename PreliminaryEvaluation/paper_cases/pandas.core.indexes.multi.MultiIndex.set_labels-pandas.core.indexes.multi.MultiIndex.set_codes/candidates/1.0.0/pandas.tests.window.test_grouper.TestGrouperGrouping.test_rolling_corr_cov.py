def test_rolling_corr_cov(self):
    g = self.frame.groupby('A')
    r = g.rolling(window=4)
    for f in ['corr', 'cov']:
        result = getattr(r, f)(self.frame)

        def func(x):
            return getattr(x.rolling(4), f)(self.frame)
        expected = g.apply(func)
        tm.assert_frame_equal(result, expected)
        result = getattr(r.B, f)(pairwise=True)

        def func(x):
            return getattr(x.B.rolling(4), f)(pairwise=True)
        expected = g.apply(func)
        tm.assert_series_equal(result, expected)