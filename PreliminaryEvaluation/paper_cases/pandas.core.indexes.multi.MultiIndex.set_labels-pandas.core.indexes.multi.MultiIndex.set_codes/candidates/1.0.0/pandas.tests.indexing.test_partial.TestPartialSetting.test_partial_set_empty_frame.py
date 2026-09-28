def test_partial_set_empty_frame(self):
    df = DataFrame()
    with pytest.raises(ValueError):
        df.loc[1] = 1
    with pytest.raises(ValueError):
        df.loc[1] = Series([1], index=['foo'])
    with pytest.raises(ValueError):
        df.loc[:, 1] = 1
    expected = DataFrame(columns=['foo'], index=Index([], dtype='object'))

    def f():
        df = DataFrame(index=Index([], dtype='object'))
        df['foo'] = Series([], dtype='object')
        return df
    tm.assert_frame_equal(f(), expected)

    def f():
        df = DataFrame()
        df['foo'] = Series(df.index)
        return df
    tm.assert_frame_equal(f(), expected)

    def f():
        df = DataFrame()
        df['foo'] = df.index
        return df
    tm.assert_frame_equal(f(), expected)
    expected = DataFrame(columns=['foo'], index=Index([], dtype='int64'))
    expected['foo'] = expected['foo'].astype('float64')

    def f():
        df = DataFrame(index=Index([], dtype='int64'))
        df['foo'] = []
        return df
    tm.assert_frame_equal(f(), expected)

    def f():
        df = DataFrame(index=Index([], dtype='int64'))
        df['foo'] = Series(np.arange(len(df)), dtype='float64')
        return df
    tm.assert_frame_equal(f(), expected)

    def f():
        df = DataFrame(index=Index([], dtype='int64'))
        df['foo'] = range(len(df))
        return df
    expected = DataFrame(columns=['foo'], index=Index([], dtype='int64'))
    expected['foo'] = expected['foo'].astype('float64')
    tm.assert_frame_equal(f(), expected)
    df = DataFrame()
    tm.assert_index_equal(df.columns, Index([], dtype=object))
    df2 = DataFrame()
    df2[1] = Series([1], index=['foo'])
    df.loc[:, 1] = Series([1], index=['foo'])
    tm.assert_frame_equal(df, DataFrame([[1]], index=['foo'], columns=[1]))
    tm.assert_frame_equal(df, df2)
    expected = DataFrame({0: Series(1, index=range(4))}, columns=['A', 'B', 0])
    df = DataFrame(columns=['A', 'B'])
    df[0] = Series(1, index=range(4))
    df.dtypes
    str(df)
    tm.assert_frame_equal(df, expected)
    df = DataFrame(columns=['A', 'B'])
    df.loc[:, 0] = Series(1, index=range(4))
    df.dtypes
    str(df)
    tm.assert_frame_equal(df, expected)