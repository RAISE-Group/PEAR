def test_multiindex_setitem(self):
    arrays = [np.array(['bar', 'bar', 'baz', 'qux', 'qux', 'bar']), np.array(['one', 'two', 'one', 'one', 'two', 'one']), np.arange(0, 6, 1)]
    df_orig = DataFrame(np.random.randn(6, 3), index=arrays, columns=['A', 'B', 'C']).sort_index()
    expected = df_orig.loc[['bar']] * 2
    df = df_orig.copy()
    df.loc[['bar']] *= 2
    tm.assert_frame_equal(df.loc[['bar']], expected)
    with pytest.raises(TypeError):
        df.loc['bar'] *= 2
    df_orig = DataFrame.from_dict({'price': {('DE', 'Coal', 'Stock'): 2, ('DE', 'Gas', 'Stock'): 4, ('DE', 'Elec', 'Demand'): 1, ('FR', 'Gas', 'Stock'): 5, ('FR', 'Solar', 'SupIm'): 0, ('FR', 'Wind', 'SupIm'): 0}})
    df_orig.index = MultiIndex.from_tuples(df_orig.index, names=['Sit', 'Com', 'Type'])
    expected = df_orig.copy()
    expected.iloc[[0, 2, 3]] *= 2
    idx = pd.IndexSlice
    df = df_orig.copy()
    df.loc[idx[:, :, 'Stock'], :] *= 2
    tm.assert_frame_equal(df, expected)
    df = df_orig.copy()
    df.loc[idx[:, :, 'Stock'], 'price'] *= 2
    tm.assert_frame_equal(df, expected)