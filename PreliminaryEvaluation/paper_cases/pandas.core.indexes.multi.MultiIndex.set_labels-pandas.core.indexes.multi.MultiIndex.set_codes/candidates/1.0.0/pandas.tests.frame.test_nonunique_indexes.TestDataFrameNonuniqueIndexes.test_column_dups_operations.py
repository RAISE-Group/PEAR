def test_column_dups_operations(self):

    def check(result, expected=None):
        if expected is not None:
            tm.assert_frame_equal(result, expected)
        result.dtypes
        str(result)
    arr = np.random.randn(3, 2)
    idx = list(range(2))
    df = DataFrame(arr, columns=['A', 'A'])
    df.columns = idx
    expected = DataFrame(arr, columns=idx)
    check(df, expected)
    idx = date_range('20130101', periods=4, freq='Q-NOV')
    df = DataFrame([[1, 1, 1, 5], [1, 1, 2, 5], [2, 1, 3, 5]], columns=['a', 'a', 'a', 'a'])
    df.columns = idx
    expected = DataFrame([[1, 1, 1, 5], [1, 1, 2, 5], [2, 1, 3, 5]], columns=idx)
    check(df, expected)
    df = DataFrame([[1, 1, 1, 5], [1, 1, 2, 5], [2, 1, 3, 5]], columns=['foo', 'bar', 'foo', 'hello'])
    df['string'] = 'bah'
    expected = DataFrame([[1, 1, 1, 5, 'bah'], [1, 1, 2, 5, 'bah'], [2, 1, 3, 5, 'bah']], columns=['foo', 'bar', 'foo', 'hello', 'string'])
    check(df, expected)
    with pytest.raises(ValueError, match='Length of value'):
        df.insert(0, 'AnotherColumn', range(len(df.index) - 1))
    df['foo2'] = 3
    expected = DataFrame([[1, 1, 1, 5, 'bah', 3], [1, 1, 2, 5, 'bah', 3], [2, 1, 3, 5, 'bah', 3]], columns=['foo', 'bar', 'foo', 'hello', 'string', 'foo2'])
    check(df, expected)
    df['foo2'] = 4
    expected = DataFrame([[1, 1, 1, 5, 'bah', 4], [1, 1, 2, 5, 'bah', 4], [2, 1, 3, 5, 'bah', 4]], columns=['foo', 'bar', 'foo', 'hello', 'string', 'foo2'])
    check(df, expected)
    df['foo2'] = 3
    del df['bar']
    expected = DataFrame([[1, 1, 5, 'bah', 3], [1, 2, 5, 'bah', 3], [2, 3, 5, 'bah', 3]], columns=['foo', 'foo', 'hello', 'string', 'foo2'])
    check(df, expected)
    del df['hello']
    expected = DataFrame([[1, 1, 'bah', 3], [1, 2, 'bah', 3], [2, 3, 'bah', 3]], columns=['foo', 'foo', 'string', 'foo2'])
    check(df, expected)
    df = df._consolidate()
    expected = DataFrame([[1, 1, 'bah', 3], [1, 2, 'bah', 3], [2, 3, 'bah', 3]], columns=['foo', 'foo', 'string', 'foo2'])
    check(df, expected)
    df.insert(2, 'new_col', 5.0)
    expected = DataFrame([[1, 1, 5.0, 'bah', 3], [1, 2, 5.0, 'bah', 3], [2, 3, 5.0, 'bah', 3]], columns=['foo', 'foo', 'new_col', 'string', 'foo2'])
    check(df, expected)
    with pytest.raises(ValueError, match='cannot insert'):
        df.insert(2, 'new_col', 4.0)
    df.insert(2, 'new_col', 4.0, allow_duplicates=True)
    expected = DataFrame([[1, 1, 4.0, 5.0, 'bah', 3], [1, 2, 4.0, 5.0, 'bah', 3], [2, 3, 4.0, 5.0, 'bah', 3]], columns=['foo', 'foo', 'new_col', 'new_col', 'string', 'foo2'])
    check(df, expected)
    del df['foo']
    expected = DataFrame([[4.0, 5.0, 'bah', 3], [4.0, 5.0, 'bah', 3], [4.0, 5.0, 'bah', 3]], columns=['new_col', 'new_col', 'string', 'foo2'])
    tm.assert_frame_equal(df, expected)
    df = DataFrame([[1, 1, 1.0, 5], [1, 1, 2.0, 5], [2, 1, 3.0, 5]], columns=['foo', 'bar', 'foo', 'hello'])
    check(df)
    df['foo2'] = 7.0
    expected = DataFrame([[1, 1, 1.0, 5, 7.0], [1, 1, 2.0, 5, 7.0], [2, 1, 3.0, 5, 7.0]], columns=['foo', 'bar', 'foo', 'hello', 'foo2'])
    check(df, expected)
    result = df['foo']
    expected = DataFrame([[1, 1.0], [1, 2.0], [2, 3.0]], columns=['foo', 'foo'])
    check(result, expected)
    df['foo'] = 'string'
    expected = DataFrame([['string', 1, 'string', 5, 7.0], ['string', 1, 'string', 5, 7.0], ['string', 1, 'string', 5, 7.0]], columns=['foo', 'bar', 'foo', 'hello', 'foo2'])
    check(df, expected)
    del df['foo']
    expected = DataFrame([[1, 5, 7.0], [1, 5, 7.0], [1, 5, 7.0]], columns=['bar', 'hello', 'foo2'])
    check(df, expected)
    df = DataFrame([[1, 2.5], [3, 4.5]], index=[1, 2], columns=['x', 'x'])
    result = df.values
    expected = np.array([[1, 2.5], [3, 4.5]])
    assert (result == expected).all().all()
    df4 = DataFrame({'RT': [0.0454], 'TClose': [22.02], 'TExg': [0.0422]}, index=MultiIndex.from_tuples([(600809, 20130331)], names=['STK_ID', 'RPT_Date']))
    df5 = DataFrame({'RPT_Date': [20120930, 20121231, 20130331], 'STK_ID': [600809] * 3, 'STK_Name': ['饡驦', '饡驦', '饡驦'], 'TClose': [38.05, 41.66, 30.01]}, index=MultiIndex.from_tuples([(600809, 20120930), (600809, 20121231), (600809, 20130331)], names=['STK_ID', 'RPT_Date']))
    k = pd.merge(df4, df5, how='inner', left_index=True, right_index=True)
    result = k.rename(columns={'TClose_x': 'TClose', 'TClose_y': 'QT_Close'})
    str(result)
    result.dtypes
    expected = DataFrame([[0.0454, 22.02, 0.0422, 20130331, 600809, '饡驦', 30.01]], columns=['RT', 'TClose', 'TExg', 'RPT_Date', 'STK_ID', 'STK_Name', 'QT_Close']).set_index(['STK_ID', 'RPT_Date'], drop=False)
    tm.assert_frame_equal(result, expected)
    df = DataFrame([[1, 5, 7.0], [1, 5, 7.0], [1, 5, 7.0]], columns=['bar', 'a', 'a'])
    msg = 'cannot reindex from a duplicate axis'
    with pytest.raises(ValueError, match=msg):
        df.reindex(columns=['bar'])
    with pytest.raises(ValueError, match=msg):
        df.reindex(columns=['bar', 'foo'])
    df = DataFrame([[1, 5, 7.0], [1, 5, 7.0], [1, 5, 7.0]], columns=['bar', 'a', 'a'])
    result = df.drop(['a'], axis=1)
    expected = DataFrame([[1], [1], [1]], columns=['bar'])
    check(result, expected)
    result = df.drop('a', axis=1)
    check(result, expected)
    df = DataFrame([[1, 1, 1], [2, 2, 2], [3, 3, 3]], columns=['bar', 'a', 'a'], dtype='float64')
    result = df.describe()
    s = df.iloc[:, 0].describe()
    expected = pd.concat([s, s, s], keys=df.columns, axis=1)
    check(result, expected)
    df = DataFrame(np.random.randn(5, 3), index=['a', 'b', 'c', 'd', 'e'], columns=['A', 'B', 'A'])
    for index in [df.index, pd.Index(list('edcba'))]:
        this_df = df.copy()
        expected_ser = pd.Series(index.values, index=this_df.index)
        expected_df = DataFrame({'A': expected_ser, 'B': this_df['B'], 'A': expected_ser}, columns=['A', 'B', 'A'])
        this_df['A'] = index
        check(this_df, expected_df)
    for op in ['__add__', '__mul__', '__sub__', '__truediv__']:
        df = DataFrame(dict(A=np.arange(10), B=np.random.rand(10)))
        expected = getattr(df, op)(df)
        expected.columns = ['A', 'A']
        df.columns = ['A', 'A']
        result = getattr(df, op)(df)
        check(result, expected)
    df = DataFrame(np.random.randn(5, 2), columns=['that', 'that'])
    expected = DataFrame(1.0, index=range(5), columns=['that', 'that'])
    df['that'] = 1.0
    check(df, expected)
    df = DataFrame(np.random.rand(5, 2), columns=['that', 'that'])
    expected = DataFrame(1, index=range(5), columns=['that', 'that'])
    df['that'] = 1
    check(df, expected)