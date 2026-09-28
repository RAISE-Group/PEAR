def test_binary_ops_align(self):
    index = MultiIndex.from_product([list('abc'), ['one', 'two', 'three'], [1, 2, 3]], names=['first', 'second', 'third'])
    df = DataFrame(np.arange(27 * 3).reshape(27, 3), index=index, columns=['value1', 'value2', 'value3']).sort_index()
    idx = pd.IndexSlice
    for op in ['add', 'sub', 'mul', 'div', 'truediv']:
        opa = getattr(operator, op, None)
        if opa is None:
            continue
        x = Series([1.0, 10.0, 100.0], [1, 2, 3])
        result = getattr(df, op)(x, level='third', axis=0)
        expected = pd.concat([opa(df.loc[idx[:, :, i], :], v) for i, v in x.items()]).sort_index()
        tm.assert_frame_equal(result, expected)
        x = Series([1.0, 10.0], ['two', 'three'])
        result = getattr(df, op)(x, level='second', axis=0)
        expected = pd.concat([opa(df.loc[idx[:, i], :], v) for i, v in x.items()]).reindex_like(df).sort_index()
        tm.assert_frame_equal(result, expected)
    midx = MultiIndex.from_product([['A', 'B'], ['a', 'b']])
    df = DataFrame(np.ones((2, 4), dtype='int64'), columns=midx)
    s = pd.Series({'a': 1, 'b': 2})
    df2 = df.copy()
    df2.columns.names = ['lvl0', 'lvl1']
    s2 = s.copy()
    s2.index.name = 'lvl1'
    res1 = df.mul(s, axis=1, level=1)
    res2 = df.mul(s2, axis=1, level=1)
    res3 = df2.mul(s, axis=1, level=1)
    res4 = df2.mul(s2, axis=1, level=1)
    res5 = df2.mul(s, axis=1, level='lvl1')
    res6 = df2.mul(s2, axis=1, level='lvl1')
    exp = DataFrame(np.array([[1, 2, 1, 2], [1, 2, 1, 2]], dtype='int64'), columns=midx)
    for res in [res1, res2]:
        tm.assert_frame_equal(res, exp)
    exp.columns.names = ['lvl0', 'lvl1']
    for res in [res3, res4, res5, res6]:
        tm.assert_frame_equal(res, exp)