def test_concat_copy(self):
    df = DataFrame(np.random.randn(4, 3))
    df2 = DataFrame(np.random.randint(0, 10, size=4).reshape(4, 1))
    df3 = DataFrame({5: 'foo'}, index=range(4))
    result = concat([df, df2, df3], axis=1, copy=True)
    for b in result._data.blocks:
        assert b.values.base is None
    result = concat([df, df2, df3], axis=1, copy=False)
    for b in result._data.blocks:
        if b.is_float:
            assert b.values.base is df._data.blocks[0].values.base
        elif b.is_integer:
            assert b.values.base is df2._data.blocks[0].values.base
        elif b.is_object:
            assert b.values.base is not None
    df4 = DataFrame(np.random.randn(4, 1))
    result = concat([df, df2, df3, df4], axis=1, copy=False)
    for b in result._data.blocks:
        if b.is_float:
            assert b.values.base is None
        elif b.is_integer:
            assert b.values.base is df2._data.blocks[0].values.base
        elif b.is_object:
            assert b.values.base is not None