def test_rolling_apply_mutability(self):
    df = pd.DataFrame({'A': ['foo'] * 3 + ['bar'] * 3, 'B': [1] * 6})
    g = df.groupby('A')
    mi = pd.MultiIndex.from_tuples([('bar', 3), ('bar', 4), ('bar', 5), ('foo', 0), ('foo', 1), ('foo', 2)])
    mi.names = ['A', None]
    expected = pd.DataFrame([np.nan, 2.0, 2.0] * 2, columns=['B'], index=mi)
    result = g.rolling(window=2).sum()
    tm.assert_frame_equal(result, expected)
    g.sum()
    result = g.rolling(window=2).sum()
    tm.assert_frame_equal(result, expected)