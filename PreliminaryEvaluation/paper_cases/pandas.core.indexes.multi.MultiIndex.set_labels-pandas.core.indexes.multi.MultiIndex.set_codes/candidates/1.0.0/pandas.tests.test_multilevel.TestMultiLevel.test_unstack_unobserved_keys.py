def test_unstack_unobserved_keys(self):
    levels = [[0, 1], [0, 1, 2, 3]]
    codes = [[0, 0, 1, 1], [0, 2, 0, 2]]
    index = MultiIndex(levels, codes)
    df = DataFrame(np.random.randn(4, 2), index=index)
    result = df.unstack()
    assert len(result.columns) == 4
    recons = result.stack()
    tm.assert_frame_equal(recons, df)