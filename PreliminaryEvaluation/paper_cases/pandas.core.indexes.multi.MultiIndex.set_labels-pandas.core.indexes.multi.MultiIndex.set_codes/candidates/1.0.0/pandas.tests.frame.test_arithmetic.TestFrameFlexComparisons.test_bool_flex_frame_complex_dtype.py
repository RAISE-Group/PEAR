def test_bool_flex_frame_complex_dtype(self):
    arr = np.array([np.nan, 1, 6, np.nan])
    arr2 = np.array([2j, np.nan, 7, None])
    df = pd.DataFrame({'a': arr})
    df2 = pd.DataFrame({'a': arr2})
    msg = '|'.join(["'>' not supported between instances of '.*' and 'complex'", 'unorderable types: .*complex\\(\\)'])
    with pytest.raises(TypeError, match=msg):
        df.gt(df2)
    with pytest.raises(TypeError, match=msg):
        df['a'].gt(df2['a'])
    with pytest.raises(TypeError, match=msg):
        df.values > df2.values
    rs = df.ne(df2)
    assert rs.values.all()
    arr3 = np.array([2j, np.nan, None])
    df3 = pd.DataFrame({'a': arr3})
    with pytest.raises(TypeError, match=msg):
        df3.gt(2j)
    with pytest.raises(TypeError, match=msg):
        df3['a'].gt(2j)
    with pytest.raises(TypeError, match=msg):
        df3.values > 2j