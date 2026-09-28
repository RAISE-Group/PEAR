def test_concat_multiindex_rangeindex(self):
    df = DataFrame(np.random.randn(9, 2))
    df.index = MultiIndex(levels=[pd.RangeIndex(3), pd.RangeIndex(3)], codes=[np.repeat(np.arange(3), 3), np.tile(np.arange(3), 3)])
    res = concat([df.iloc[[2, 3, 4], :], df.iloc[[5], :]])
    exp = df.iloc[[2, 3, 4, 5], :]
    tm.assert_frame_equal(res, exp)