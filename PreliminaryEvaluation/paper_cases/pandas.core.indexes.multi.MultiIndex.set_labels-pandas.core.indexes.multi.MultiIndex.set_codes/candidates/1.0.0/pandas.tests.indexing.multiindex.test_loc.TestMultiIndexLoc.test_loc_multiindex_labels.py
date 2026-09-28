def test_loc_multiindex_labels(self):
    df = DataFrame(np.random.randn(3, 3), columns=[['i', 'i', 'j'], ['A', 'A', 'B']], index=[['i', 'i', 'j'], ['X', 'X', 'Y']])
    expected = df.iloc[[0, 1]].droplevel(0)
    result = df.loc['i']
    tm.assert_frame_equal(result, expected)
    expected = df.iloc[:, [2]].droplevel(0, axis=1)
    result = df.loc[:, 'j']
    tm.assert_frame_equal(result, expected)
    expected = df.iloc[[2], [2]].droplevel(0).droplevel(0, axis=1)
    result = df.loc['j'].loc[:, 'j']
    tm.assert_frame_equal(result, expected)
    expected = df.iloc[[0, 1]]
    result = df.loc['i', 'X']
    tm.assert_frame_equal(result, expected)