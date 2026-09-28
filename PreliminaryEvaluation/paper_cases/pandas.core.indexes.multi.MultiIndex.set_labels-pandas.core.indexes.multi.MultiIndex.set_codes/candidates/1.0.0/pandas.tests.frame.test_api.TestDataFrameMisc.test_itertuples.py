def test_itertuples(self, float_frame):
    for i, tup in enumerate(float_frame.itertuples()):
        s = DataFrame._constructor_sliced(tup[1:])
        s.name = tup[0]
        expected = float_frame.iloc[i, :].reset_index(drop=True)
        tm.assert_series_equal(s, expected)
    df = DataFrame({'floats': np.random.randn(5), 'ints': range(5)}, columns=['floats', 'ints'])
    for tup in df.itertuples(index=False):
        assert isinstance(tup[1], int)
    df = DataFrame(data={'a': [1, 2, 3], 'b': [4, 5, 6]})
    dfaa = df[['a', 'a']]
    assert list(dfaa.itertuples()) == [(0, 1, 1), (1, 2, 2), (2, 3, 3)]
    if not (compat.is_platform_windows() or compat.is_platform_32bit()):
        assert repr(list(df.itertuples(name=None))) == '[(0, 1, 4), (1, 2, 5), (2, 3, 6)]'
    tup = next(df.itertuples(name='TestName'))
    assert tup._fields == ('Index', 'a', 'b')
    assert (tup.Index, tup.a, tup.b) == tup
    assert type(tup).__name__ == 'TestName'
    df.columns = ['def', 'return']
    tup2 = next(df.itertuples(name='TestName'))
    assert tup2 == (0, 1, 4)
    assert tup2._fields == ('Index', '_1', '_2')
    df3 = DataFrame({'f' + str(i): [i] for i in range(1024)})
    tup3 = next(df3.itertuples())
    assert isinstance(tup3, tuple)
    if PY37:
        assert hasattr(tup3, '_fields')
    else:
        assert not hasattr(tup3, '_fields')
    df_254_columns = DataFrame([{f'foo_{i}': f'bar_{i}' for i in range(254)}])
    result_254_columns = next(df_254_columns.itertuples(index=False))
    assert isinstance(result_254_columns, tuple)
    assert hasattr(result_254_columns, '_fields')
    df_255_columns = DataFrame([{f'foo_{i}': f'bar_{i}' for i in range(255)}])
    result_255_columns = next(df_255_columns.itertuples(index=False))
    assert isinstance(result_255_columns, tuple)
    if PY37:
        assert hasattr(result_255_columns, '_fields')
    else:
        assert not hasattr(result_255_columns, '_fields')