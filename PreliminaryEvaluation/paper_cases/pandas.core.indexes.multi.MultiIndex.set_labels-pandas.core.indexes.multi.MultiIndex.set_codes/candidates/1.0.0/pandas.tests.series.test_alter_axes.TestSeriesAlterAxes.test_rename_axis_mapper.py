def test_rename_axis_mapper(self):
    mi = MultiIndex.from_product([['a', 'b', 'c'], [1, 2]], names=['ll', 'nn'])
    s = Series(list(range(len(mi))), index=mi)
    result = s.rename_axis(index={'ll': 'foo'})
    assert result.index.names == ['foo', 'nn']
    result = s.rename_axis(index=str.upper, axis=0)
    assert result.index.names == ['LL', 'NN']
    result = s.rename_axis(index=['foo', 'goo'])
    assert result.index.names == ['foo', 'goo']
    with pytest.raises(TypeError, match='unexpected'):
        s.rename_axis(columns='wrong')