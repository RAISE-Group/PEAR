def test_inplace_ops_identity(self):
    s_orig = Series([1, 2, 3])
    df_orig = DataFrame(np.random.randint(0, 5, size=10).reshape(-1, 5))
    s = s_orig.copy()
    s2 = s
    s += 1
    tm.assert_series_equal(s, s2)
    tm.assert_series_equal(s_orig + 1, s)
    assert s is s2
    assert s._data is s2._data
    df = df_orig.copy()
    df2 = df
    df += 1
    tm.assert_frame_equal(df, df2)
    tm.assert_frame_equal(df_orig + 1, df)
    assert df is df2
    assert df._data is df2._data
    s = s_orig.copy()
    s2 = s
    s += 1.5
    tm.assert_series_equal(s, s2)
    tm.assert_series_equal(s_orig + 1.5, s)
    df = df_orig.copy()
    df2 = df
    df += 1.5
    tm.assert_frame_equal(df, df2)
    tm.assert_frame_equal(df_orig + 1.5, df)
    assert df is df2
    assert df._data is df2._data
    arr = np.random.randint(0, 10, size=5)
    df_orig = DataFrame({'A': arr.copy(), 'B': 'foo'})
    df = df_orig.copy()
    df2 = df
    df['A'] += 1
    expected = DataFrame({'A': arr.copy() + 1, 'B': 'foo'})
    tm.assert_frame_equal(df, expected)
    tm.assert_frame_equal(df2, expected)
    assert df._data is df2._data
    df = df_orig.copy()
    df2 = df
    df['A'] += 1.5
    expected = DataFrame({'A': arr.copy() + 1.5, 'B': 'foo'})
    tm.assert_frame_equal(df, expected)
    tm.assert_frame_equal(df2, expected)
    assert df._data is df2._data