def test_set_index_names(self):
    df = tm.makeDataFrame()
    df.index.name = 'name'
    assert df.set_index(df.index).index.names == ['name']
    mi = MultiIndex.from_arrays(df[['A', 'B']].T.values, names=['A', 'B'])
    mi2 = MultiIndex.from_arrays(df[['A', 'B', 'A', 'B']].T.values, names=['A', 'B', 'C', 'D'])
    df = df.set_index(['A', 'B'])
    assert df.set_index(df.index).index.names == ['A', 'B']
    assert isinstance(df.set_index(df.index).index, MultiIndex)
    tm.assert_index_equal(df.set_index(df.index).index, mi)
    idx2 = df.index.rename(['C', 'D'])
    assert isinstance(df.set_index([df.index, idx2]).index, MultiIndex)
    tm.assert_index_equal(df.set_index([df.index, idx2]).index, mi2)