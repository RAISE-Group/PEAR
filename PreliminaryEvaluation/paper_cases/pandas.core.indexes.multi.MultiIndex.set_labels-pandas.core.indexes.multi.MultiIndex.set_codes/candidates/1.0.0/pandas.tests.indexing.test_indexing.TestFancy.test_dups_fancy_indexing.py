def test_dups_fancy_indexing(self):
    df = tm.makeCustomDataframe(10, 3)
    df.columns = ['a', 'a', 'b']
    result = df[['b', 'a']].columns
    expected = Index(['b', 'a', 'a'])
    tm.assert_index_equal(result, expected)
    df = DataFrame([[1, 2, 1.0, 2.0, 3.0, 'foo', 'bar']], columns=list('aaaaaaa'))
    df.head()
    str(df)
    result = DataFrame([[1, 2, 1.0, 2.0, 3.0, 'foo', 'bar']])
    result.columns = list('aaaaaaa')
    df_v = df.iloc[:, 4]
    res_v = result.iloc[:, 4]
    tm.assert_frame_equal(df, result)
    df = DataFrame({'test': [5, 7, 9, 11], 'test1': [4.0, 5, 6, 7], 'other': list('abcd')}, index=['A', 'A', 'B', 'C'])
    rows = ['C', 'B']
    expected = DataFrame({'test': [11, 9], 'test1': [7.0, 6], 'other': ['d', 'c']}, index=rows)
    result = df.loc[rows]
    tm.assert_frame_equal(result, expected)
    result = df.loc[Index(rows)]
    tm.assert_frame_equal(result, expected)
    rows = ['C', 'B', 'E']
    with pytest.raises(KeyError, match='with any missing labels'):
        df.loc[rows]
    rows = ['F', 'G', 'H', 'C', 'B', 'E']
    with pytest.raises(KeyError, match='with any missing labels'):
        df.loc[rows]
    dfnu = DataFrame(np.random.randn(5, 3), index=list('AABCD'))
    with pytest.raises(KeyError, match=re.escape('"None of [Index([\'E\'], dtype=\'object\')] are in the [index]"')):
        dfnu.loc[['E']]
    df = DataFrame({'A': [0, 1, 2]})
    with pytest.raises(KeyError, match='with any missing labels'):
        df.loc[[0, 8, 0]]
    df = DataFrame({'A': list('abc')})
    with pytest.raises(KeyError, match='with any missing labels'):
        df.loc[[0, 8, 0]]
    df = DataFrame({'test': [5, 7, 9, 11]}, index=['A', 'A', 'B', 'C'])
    with pytest.raises(KeyError, match='with any missing labels'):
        df.loc[['A', 'A', 'E']]