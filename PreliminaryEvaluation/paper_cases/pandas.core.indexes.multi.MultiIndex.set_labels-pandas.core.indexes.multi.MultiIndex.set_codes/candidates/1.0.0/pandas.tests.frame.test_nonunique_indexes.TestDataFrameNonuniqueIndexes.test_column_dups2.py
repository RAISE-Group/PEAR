def test_column_dups2(self):
    df = DataFrame({'A': np.random.randn(5), 'B': np.random.randn(5), 'C': np.random.randn(5), 'D': ['a', 'b', 'c', 'd', 'e']})
    expected = df.take([0, 1, 1], axis=1)
    df2 = df.take([2, 0, 1, 2, 1], axis=1)
    result = df2.drop('C', axis=1)
    tm.assert_frame_equal(result, expected)
    df = DataFrame({'A': np.random.randn(5), 'B': np.random.randn(5), 'C': np.random.randn(5), 'D': ['a', 'b', 'c', 'd', 'e']})
    df.iloc[2, [0, 1, 2]] = np.nan
    df.iloc[0, 0] = np.nan
    df.iloc[1, 1] = np.nan
    df.iloc[:, 3] = np.nan
    expected = df.dropna(subset=['A', 'B', 'C'], how='all')
    expected.columns = ['A', 'A', 'B', 'C']
    df.columns = ['A', 'A', 'B', 'C']
    result = df.dropna(subset=['A', 'C'], how='all')
    tm.assert_frame_equal(result, expected)