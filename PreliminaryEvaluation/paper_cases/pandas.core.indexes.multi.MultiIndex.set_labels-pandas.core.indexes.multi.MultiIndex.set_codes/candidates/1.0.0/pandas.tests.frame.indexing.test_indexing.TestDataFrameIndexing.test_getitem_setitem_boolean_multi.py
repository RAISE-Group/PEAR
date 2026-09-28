def test_getitem_setitem_boolean_multi(self):
    df = DataFrame(np.random.randn(3, 2))
    k1 = np.array([True, False, True])
    k2 = np.array([False, True])
    result = df.loc[k1, k2]
    expected = df.loc[[0, 2], [1]]
    tm.assert_frame_equal(result, expected)
    expected = df.copy()
    df.loc[np.array([True, False, True]), np.array([False, True])] = 5
    expected.loc[[0, 2], [1]] = 5
    tm.assert_frame_equal(df, expected)