def test_loc_indexing_preserves_index_category_dtype(self):
    df = DataFrame(data=np.arange(2, 22, 2), index=pd.MultiIndex(levels=[pd.CategoricalIndex(['a', 'b']), range(10)], codes=[[0] * 5 + [1] * 5, range(10)], names=['Index1', 'Index2']))
    expected = pd.CategoricalIndex(['a', 'b'], categories=['a', 'b'], ordered=False, name='Index1', dtype='category')
    result = df.index.levels[0]
    tm.assert_index_equal(result, expected)
    result = df.loc[['a']].index.levels[0]
    tm.assert_index_equal(result, expected)