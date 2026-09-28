def test_add_column_with_pandas_array(self):
    df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': ['a', 'b', 'c', 'd']})
    df['c'] = pd.arrays.PandasArray(np.array([1, 2, None, 3], dtype=object))
    df2 = pd.DataFrame({'a': [1, 2, 3, 4], 'b': ['a', 'b', 'c', 'd'], 'c': pd.arrays.PandasArray(np.array([1, 2, None, 3], dtype=object))})
    assert type(df['c']._data.blocks[0]) == ObjectBlock
    assert type(df2['c']._data.blocks[0]) == ObjectBlock
    tm.assert_frame_equal(df, df2)