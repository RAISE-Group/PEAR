def test_insert(self):
    df = DataFrame(np.random.randn(5, 3), index=np.arange(5), columns=['c', 'b', 'a'])
    df.insert(0, 'foo', df['a'])
    tm.assert_index_equal(df.columns, Index(['foo', 'c', 'b', 'a']))
    tm.assert_series_equal(df['a'], df['foo'], check_names=False)
    df.insert(2, 'bar', df['c'])
    tm.assert_index_equal(df.columns, Index(['foo', 'c', 'bar', 'b', 'a']))
    tm.assert_almost_equal(df['c'], df['bar'], check_names=False)
    df['x'] = df['a'].astype('float32')
    result = df.dtypes
    expected = Series([np.dtype('float64')] * 5 + [np.dtype('float32')], index=['foo', 'c', 'bar', 'b', 'a', 'x'])
    tm.assert_series_equal(result, expected)
    df['a'] = df['a'].astype('float32')
    result = df.dtypes
    expected = Series([np.dtype('float64')] * 4 + [np.dtype('float32')] * 2, index=['foo', 'c', 'bar', 'b', 'a', 'x'])
    tm.assert_series_equal(result, expected)
    df['y'] = df['a'].astype('int32')
    result = df.dtypes
    expected = Series([np.dtype('float64')] * 4 + [np.dtype('float32')] * 2 + [np.dtype('int32')], index=['foo', 'c', 'bar', 'b', 'a', 'x', 'y'])
    tm.assert_series_equal(result, expected)
    with pytest.raises(ValueError, match='already exists'):
        df.insert(1, 'a', df['b'])
    msg = 'cannot insert c, already exists'
    with pytest.raises(ValueError, match=msg):
        df.insert(1, 'c', df['b'])
    df.columns.name = 'some_name'
    df.insert(0, 'baz', df['c'])
    assert df.columns.name == 'some_name'
    df = DataFrame(index=['A', 'B', 'C'])
    df['X'] = df.index
    df['X'] = ['x', 'y', 'z']
    exp = DataFrame(data={'X': ['x', 'y', 'z']}, index=['A', 'B', 'C'])
    tm.assert_frame_equal(df, exp)