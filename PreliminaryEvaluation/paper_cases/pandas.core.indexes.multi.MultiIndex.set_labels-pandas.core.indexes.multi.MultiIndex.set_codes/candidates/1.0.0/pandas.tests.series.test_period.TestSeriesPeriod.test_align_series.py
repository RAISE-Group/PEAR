def test_align_series(self, join_type):
    rng = period_range('1/1/2000', '1/1/2010', freq='A')
    ts = Series(np.random.randn(len(rng)), index=rng)
    ts.align(ts[::2], join=join_type)