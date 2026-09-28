def test_column_dups_indexing(self):

    def check(result, expected=None):
        if expected is not None:
            tm.assert_frame_equal(result, expected)
        result.dtypes
        str(result)
    dups = ['A', 'A', 'C', 'D']
    df = DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'], dtype='float64')
    expected = df[df.C > 6]
    expected.columns = dups
    df = DataFrame(np.arange(12).reshape(3, 4), columns=dups, dtype='float64')
    result = df[df.C > 6]
    check(result, expected)
    df = DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'], dtype='float64')
    expected = df[df > 6]
    expected.columns = dups
    df = DataFrame(np.arange(12).reshape(3, 4), columns=dups, dtype='float64')
    result = df[df > 6]
    check(result, expected)
    df = DataFrame(np.arange(12).reshape(3, 4), columns=dups, dtype='float64')
    msg = 'cannot reindex from a duplicate axis'
    with pytest.raises(ValueError, match=msg):
        df[df.A > 6]
    df1 = DataFrame([1, 2, 3, 4, 5], index=[1, 2, 1, 2, 3])
    df2 = DataFrame([1, 2, 3], index=[1, 2, 3])
    expected = DataFrame([0, 2, 0, 2, 2], index=[1, 1, 2, 2, 3])
    result = df1.sub(df2)
    tm.assert_frame_equal(result, expected)
    df1 = DataFrame([[1, 2], [2, np.nan], [3, 4], [4, 4]], columns=['A', 'B'])
    df2 = DataFrame([[0, 1], [2, 4], [2, np.nan], [4, 5]], columns=['A', 'A'])
    msg = 'Can only compare identically-labeled DataFrame objects'
    with pytest.raises(ValueError, match=msg):
        df1 == df2
    df1r = df1.reindex_like(df2)
    result = df1r == df2
    expected = DataFrame([[False, True], [True, False], [False, False], [True, False]], columns=['A', 'A'])
    tm.assert_frame_equal(result, expected)
    dfbool = DataFrame({'one': Series([True, True, False], index=['a', 'b', 'c']), 'two': Series([False, False, True, False], index=['a', 'b', 'c', 'd']), 'three': Series([False, True, True, True], index=['a', 'b', 'c', 'd'])})
    expected = pd.concat([dfbool['one'], dfbool['three'], dfbool['one']], axis=1)
    result = dfbool[['one', 'three', 'one']]
    check(result, expected)
    df = DataFrame(np.arange(25.0).reshape(5, 5), index=['a', 'b', 'c', 'd', 'e'], columns=['A', 'B', 'C', 'D', 'E'])
    z = df[['A', 'C', 'A']].copy()
    expected = z.loc[['a', 'c', 'a']]
    df = DataFrame(np.arange(25.0).reshape(5, 5), index=['a', 'b', 'c', 'd', 'e'], columns=['A', 'B', 'C', 'D', 'E'])
    z = df[['A', 'C', 'A']]
    result = z.loc[['a', 'c', 'a']]
    check(result, expected)