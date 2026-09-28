def test_per_axis_per_level_doc_examples(self):
    idx = pd.IndexSlice
    index = MultiIndex.from_product([_mklbl('A', 4), _mklbl('B', 2), _mklbl('C', 4), _mklbl('D', 2)])
    columns = MultiIndex.from_tuples([('a', 'foo'), ('a', 'bar'), ('b', 'foo'), ('b', 'bah')], names=['lvl0', 'lvl1'])
    df = DataFrame(np.arange(len(index) * len(columns), dtype='int64').reshape((len(index), len(columns))), index=index, columns=columns)
    result = df.loc[(slice('A1', 'A3'), slice(None), ['C1', 'C3']), :]
    expected = df.loc[[tuple([a, b, c, d]) for a, b, c, d in df.index.values if (a == 'A1' or a == 'A2' or a == 'A3') and (c == 'C1' or c == 'C3')]]
    tm.assert_frame_equal(result, expected)
    result = df.loc[idx['A1':'A3', :, ['C1', 'C3']], :]
    tm.assert_frame_equal(result, expected)
    result = df.loc[(slice(None), slice(None), ['C1', 'C3']), :]
    expected = df.loc[[tuple([a, b, c, d]) for a, b, c, d in df.index.values if c == 'C1' or c == 'C3']]
    tm.assert_frame_equal(result, expected)
    result = df.loc[idx[:, :, ['C1', 'C3']], :]
    tm.assert_frame_equal(result, expected)
    with pytest.raises(UnsortedIndexError):
        df.loc['A1', ('a', slice('foo'))]
    tm.assert_frame_equal(df.loc['A1', (slice(None), 'foo')], df.loc['A1'].iloc[:, [0, 2]])
    df = df.sort_index(axis=1)
    df.loc['A1', (slice(None), 'foo')]
    df.loc[(slice(None), slice(None), ['C1', 'C3']), (slice(None), 'foo')]
    df.loc(axis=0)[:, :, ['C1', 'C3']] = -10