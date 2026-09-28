def test_multi_assign(self):
    df = DataFrame({'FC': ['a', 'b', 'a', 'b', 'a', 'b'], 'PF': [0, 0, 0, 0, 1, 1], 'col1': list(range(6)), 'col2': list(range(6, 12))})
    df.iloc[1, 0] = np.nan
    df2 = df.copy()
    mask = ~df2.FC.isna()
    cols = ['col1', 'col2']
    dft = df2 * 2
    dft.iloc[3, 3] = np.nan
    expected = DataFrame({'FC': ['a', np.nan, 'a', 'b', 'a', 'b'], 'PF': [0, 0, 0, 0, 1, 1], 'col1': Series([0, 1, 4, 6, 8, 10]), 'col2': [12, 7, 16, np.nan, 20, 22]})
    df2.loc[mask, cols] = dft.loc[mask, cols]
    tm.assert_frame_equal(df2, expected)
    df2.loc[mask, cols] = dft.loc[mask, cols]
    tm.assert_frame_equal(df2, expected)
    expected = DataFrame({'FC': ['a', np.nan, 'a', 'b', 'a', 'b'], 'PF': [0, 0, 0, 0, 1, 1], 'col1': [0.0, 1.0, 4.0, 6.0, 8.0, 10.0], 'col2': [12, 7, 16, np.nan, 20, 22]})
    df2 = df.copy()
    df2.loc[mask, cols] = dft.loc[mask, cols].values
    tm.assert_frame_equal(df2, expected)
    df2.loc[mask, cols] = dft.loc[mask, cols].values
    tm.assert_frame_equal(df2, expected)
    df = DataFrame(dict(A=[1, 2, 0, 0, 0], B=[0, 0, 0, 10, 11], C=[0, 0, 0, 10, 11], D=[3, 4, 5, 6, 7]))
    expected = df.copy()
    mask = expected['A'] == 0
    for col in ['A', 'B']:
        expected.loc[mask, col] = df['D']
    df.loc[df['A'] == 0, ['A', 'B']] = df['D']
    tm.assert_frame_equal(df, expected)