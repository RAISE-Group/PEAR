def test_type_error_multiindex(self):
    df = DataFrame(columns=['i', 'c', 'x', 'y'], data=[[0, 0, 1, 2], [1, 0, 3, 4], [0, 1, 1, 2], [1, 1, 3, 4]])
    dg = df.pivot_table(index='i', columns='c', values=['x', 'y'])
    with pytest.raises(TypeError, match='is an invalid key'):
        str(dg[:, 0])
    index = Index(range(2), name='i')
    columns = MultiIndex(levels=[['x', 'y'], [0, 1]], codes=[[0, 1], [0, 0]], names=[None, 'c'])
    expected = DataFrame([[1, 2], [3, 4]], columns=columns, index=index)
    result = dg.loc[:, (slice(None), 0)]
    tm.assert_frame_equal(result, expected)
    name = ('x', 0)
    index = Index(range(2), name='i')
    expected = Series([1, 3], index=index, name=name)
    result = dg['x', 0]
    tm.assert_series_equal(result, expected)