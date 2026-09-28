def test_loc_axis_arguments(self):
    index = MultiIndex.from_product([_mklbl('A', 4), _mklbl('B', 2), _mklbl('C', 4), _mklbl('D', 2)])
    columns = MultiIndex.from_tuples([('a', 'foo'), ('a', 'bar'), ('b', 'foo'), ('b', 'bah')], names=['lvl0', 'lvl1'])
    df = DataFrame(np.arange(len(index) * len(columns), dtype='int64').reshape((len(index), len(columns))), index=index, columns=columns).sort_index().sort_index(axis=1)
    result = df.loc(axis=0)['A1':'A3', :, ['C1', 'C3']]
    expected = df.loc[[tuple([a, b, c, d]) for a, b, c, d in df.index.values if (a == 'A1' or a == 'A2' or a == 'A3') and (c == 'C1' or c == 'C3')]]
    tm.assert_frame_equal(result, expected)
    result = df.loc(axis='index')[:, :, ['C1', 'C3']]
    expected = df.loc[[tuple([a, b, c, d]) for a, b, c, d in df.index.values if c == 'C1' or c == 'C3']]
    tm.assert_frame_equal(result, expected)
    result = df.loc(axis=1)[:, 'foo']
    expected = df.loc[:, (slice(None), 'foo')]
    tm.assert_frame_equal(result, expected)
    result = df.loc(axis='columns')[:, 'foo']
    expected = df.loc[:, (slice(None), 'foo')]
    tm.assert_frame_equal(result, expected)
    with pytest.raises(ValueError):
        df.loc(axis=-1)[:, :, ['C1', 'C3']]
    with pytest.raises(ValueError):
        df.loc(axis=2)[:, :, ['C1', 'C3']]
    with pytest.raises(ValueError):
        df.loc(axis='foo')[:, :, ['C1', 'C3']]