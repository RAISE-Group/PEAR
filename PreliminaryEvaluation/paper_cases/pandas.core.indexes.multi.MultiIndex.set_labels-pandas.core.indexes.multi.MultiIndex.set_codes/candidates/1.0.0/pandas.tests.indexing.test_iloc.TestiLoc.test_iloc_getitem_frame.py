def test_iloc_getitem_frame(self):
    df = DataFrame(np.random.randn(10, 4), index=range(0, 20, 2), columns=range(0, 8, 2))
    result = df.iloc[2]
    exp = df.loc[4]
    tm.assert_series_equal(result, exp)
    result = df.iloc[2, 2]
    exp = df.loc[4, 4]
    assert result == exp
    result = df.iloc[4:8]
    expected = df.loc[8:14]
    tm.assert_frame_equal(result, expected)
    result = df.iloc[:, 2:3]
    expected = df.loc[:, 4:5]
    tm.assert_frame_equal(result, expected)
    result = df.iloc[[0, 1, 3]]
    expected = df.loc[[0, 2, 6]]
    tm.assert_frame_equal(result, expected)
    result = df.iloc[[0, 1, 3], [0, 1]]
    expected = df.loc[[0, 2, 6], [0, 2]]
    tm.assert_frame_equal(result, expected)
    result = df.iloc[[-1, 1, 3], [-1, 1]]
    expected = df.loc[[18, 2, 6], [6, 2]]
    tm.assert_frame_equal(result, expected)
    result = df.iloc[[-1, -1, 1, 3], [-1, 1]]
    expected = df.loc[[18, 18, 2, 6], [6, 2]]
    tm.assert_frame_equal(result, expected)
    s = Series(index=range(1, 5), dtype=object)
    result = df.iloc[s.index]
    expected = df.loc[[2, 4, 6, 8]]
    tm.assert_frame_equal(result, expected)