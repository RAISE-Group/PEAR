def test_mask(self):
    df = DataFrame(np.random.randn(5, 3))
    cond = df > 0
    rs = df.where(cond, np.nan)
    tm.assert_frame_equal(rs, df.mask(df <= 0))
    tm.assert_frame_equal(rs, df.mask(~cond))
    other = DataFrame(np.random.randn(5, 3))
    rs = df.where(cond, other)
    tm.assert_frame_equal(rs, df.mask(df <= 0, other))
    tm.assert_frame_equal(rs, df.mask(~cond, other))
    df = DataFrame([1, 2])
    res = df.mask([[True], [False]])
    exp = DataFrame([np.nan, 2])
    tm.assert_frame_equal(res, exp)