def test_expanding_corr_cov(self):
    g = self.frame.groupby('A')
    r = g.expanding()
    for f in ['corr', 'cov']:
        result = getattr(r, f)(self.frame)

        def func(x):
            return getattr(x.expanding(), f)(self.frame)
        expected = g.apply(func)
        tm.assert_frame_equal(result, expected)
        result = getattr(r.B, f)(pairwise=True)

        def func(x):
            return getattr(x.B.expanding(), f)(pairwise=True)
        expected = g.apply(func)
        tm.assert_series_equal(result, expected)