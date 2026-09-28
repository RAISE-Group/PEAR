def test_mask_inplace(self):
    df = DataFrame(np.random.randn(5, 3))
    cond = df > 0
    rdf = df.copy()
    rdf.where(cond, inplace=True)
    tm.assert_frame_equal(rdf, df.where(cond))
    tm.assert_frame_equal(rdf, df.mask(~cond))
    rdf = df.copy()
    rdf.where(cond, -df, inplace=True)
    tm.assert_frame_equal(rdf, df.where(cond, -df))
    tm.assert_frame_equal(rdf, df.mask(~cond, -df))