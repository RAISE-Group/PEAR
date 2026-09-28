def test_multiindex_assignment(self):
    df = DataFrame(np.random.randint(5, 10, size=9).reshape(3, 3), columns=list('abc'), index=[[4, 4, 8], [8, 10, 12]])
    df['d'] = np.nan
    arr = np.array([0.0, 1.0])
    df.loc[4, 'd'] = arr
    tm.assert_series_equal(df.loc[4, 'd'], Series(arr, index=[8, 10], name='d'))
    df = DataFrame(np.random.randint(5, 10, size=9).reshape(3, 3), columns=list('abc'), index=[[4, 4, 8], [8, 10, 12]])
    df.loc[4, 'c'] = arr
    exp = Series(arr, index=[8, 10], name='c', dtype='float64')
    tm.assert_series_equal(df.loc[4, 'c'], exp)
    df.loc[4, 'c'] = 10
    exp = Series(10, index=[8, 10], name='c', dtype='float64')
    tm.assert_series_equal(df.loc[4, 'c'], exp)
    with pytest.raises(ValueError):
        df.loc[4, 'c'] = [0, 1, 2, 3]
    with pytest.raises(ValueError):
        df.loc[4, 'c'] = [0]
    NUM_ROWS = 100
    NUM_COLS = 10
    col_names = ['A' + num for num in map(str, np.arange(NUM_COLS).tolist())]
    index_cols = col_names[:5]
    df = DataFrame(np.random.randint(5, size=(NUM_ROWS, NUM_COLS)), dtype=np.int64, columns=col_names)
    df = df.set_index(index_cols).sort_index()
    grp = df.groupby(level=index_cols[:4])
    df['new_col'] = np.nan
    f_index = np.arange(5)

    def f(name, df2):
        return Series(np.arange(df2.shape[0]), name=df2.index.values[0]).reindex(f_index)
    for name, df2 in grp:
        new_vals = np.arange(df2.shape[0])
        df.loc[name, 'new_col'] = new_vals