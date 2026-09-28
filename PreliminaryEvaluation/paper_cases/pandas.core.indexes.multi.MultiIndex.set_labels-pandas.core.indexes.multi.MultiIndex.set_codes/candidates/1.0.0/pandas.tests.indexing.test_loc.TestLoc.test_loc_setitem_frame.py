def test_loc_setitem_frame(self):
    df = self.frame_labels
    result = df.iloc[0, 0]
    df.loc['a', 'A'] = 1
    result = df.loc['a', 'A']
    assert result == 1
    result = df.iloc[0, 0]
    assert result == 1
    df.loc[:, 'B':'D'] = 0
    expected = df.loc[:, 'B':'D']
    result = df.iloc[:, 1:]
    tm.assert_frame_equal(result, expected)
    df = DataFrame(index=[3, 5, 4], columns=['A'])
    df.loc[[4, 3, 5], 'A'] = np.array([1, 2, 3], dtype='int64')
    expected = DataFrame(dict(A=Series([1, 2, 3], index=[4, 3, 5]))).reindex(index=[3, 5, 4])
    tm.assert_frame_equal(df, expected)
    keys1 = ['@' + str(i) for i in range(5)]
    val1 = np.arange(5, dtype='int64')
    keys2 = ['@' + str(i) for i in range(4)]
    val2 = np.arange(4, dtype='int64')
    index = list(set(keys1).union(keys2))
    df = DataFrame(index=index)
    df['A'] = np.nan
    df.loc[keys1, 'A'] = val1
    df['B'] = np.nan
    df.loc[keys2, 'B'] = val2
    expected = DataFrame(dict(A=Series(val1, index=keys1), B=Series(val2, index=keys2))).reindex(index=index)
    tm.assert_frame_equal(df, expected)
    df = DataFrame({'A': [1, 2, 3], 'B': np.nan})
    df.loc[df.B > df.A, 'B'] = df.A
    expected = DataFrame({'A': [1, 2, 3], 'B': np.nan})
    tm.assert_frame_equal(df, expected)
    df = DataFrame({1: [1, 2], 2: [3, 4], 'a': ['a', 'b']})
    result = df.loc[0, [1, 2]]
    expected = Series([1, 3], index=[1, 2], dtype=object, name=0)
    tm.assert_series_equal(result, expected)
    expected = DataFrame({1: [5, 2], 2: [6, 4], 'a': ['a', 'b']})
    df.loc[0, [1, 2]] = [5, 6]
    tm.assert_frame_equal(df, expected)