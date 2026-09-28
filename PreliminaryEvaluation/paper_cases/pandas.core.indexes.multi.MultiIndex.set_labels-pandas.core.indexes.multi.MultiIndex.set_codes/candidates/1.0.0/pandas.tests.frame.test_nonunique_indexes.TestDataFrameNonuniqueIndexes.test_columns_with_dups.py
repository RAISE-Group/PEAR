def test_columns_with_dups(self):
    df = DataFrame([[1, 2]], columns=['a', 'a'])
    df.columns = ['a', 'a.1']
    str(df)
    expected = DataFrame([[1, 2]], columns=['a', 'a.1'])
    tm.assert_frame_equal(df, expected)
    df = DataFrame([[1, 2, 3]], columns=['b', 'a', 'a'])
    df.columns = ['b', 'a', 'a.1']
    str(df)
    expected = DataFrame([[1, 2, 3]], columns=['b', 'a', 'a.1'])
    tm.assert_frame_equal(df, expected)
    df = DataFrame([[1, 2]], columns=['a', 'a'])
    df.columns = ['b', 'b']
    str(df)
    expected = DataFrame([[1, 2]], columns=['b', 'b'])
    tm.assert_frame_equal(df, expected)
    df = DataFrame([[1, 2, 1.0, 2.0, 3.0, 'foo', 'bar']], columns=['a', 'a', 'b', 'b', 'd', 'c', 'c'])
    df.columns = list('ABCDEFG')
    str(df)
    expected = DataFrame([[1, 2, 1.0, 2.0, 3.0, 'foo', 'bar']], columns=list('ABCDEFG'))
    tm.assert_frame_equal(df, expected)
    df = DataFrame([[1, 2, 'foo', 'bar']], columns=['a', 'a', 'a', 'a'])
    df.columns = ['a', 'a.1', 'a.2', 'a.3']
    str(df)
    expected = DataFrame([[1, 2, 'foo', 'bar']], columns=['a', 'a.1', 'a.2', 'a.3'])
    tm.assert_frame_equal(df, expected)
    df_float = DataFrame(np.random.randn(10, 3), dtype='float64')
    df_int = DataFrame(np.random.randn(10, 3), dtype='int64')
    df_bool = DataFrame(True, index=df_float.index, columns=df_float.columns)
    df_object = DataFrame('foo', index=df_float.index, columns=df_float.columns)
    df_dt = DataFrame(pd.Timestamp('20010101'), index=df_float.index, columns=df_float.columns)
    df = pd.concat([df_float, df_int, df_bool, df_object, df_dt], axis=1)
    assert len(df._data._blknos) == len(df.columns)
    assert len(df._data._blklocs) == len(df.columns)
    for i in range(len(df.columns)):
        df.iloc[:, i]
    vals = [[1, -1, 2.0], [2, -2, 3.0]]
    rs = DataFrame(vals, columns=['A', 'A', 'B'])
    xp = DataFrame(vals)
    xp.columns = ['A', 'A', 'B']
    tm.assert_frame_equal(rs, xp)