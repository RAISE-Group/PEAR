def test_column_multiindex(self, setup_path):
    index = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'a'), ('B', 'b')], names=['first', 'second'])
    df = DataFrame(np.arange(12).reshape(3, 4), columns=index)
    expected = df.copy()
    if isinstance(expected.index, RangeIndex):
        expected.index = Int64Index(expected.index)
    with ensure_clean_store(setup_path) as store:
        store.put('df', df)
        tm.assert_frame_equal(store['df'], expected, check_index_type=True, check_column_type=True)
        store.put('df1', df, format='table')
        tm.assert_frame_equal(store['df1'], expected, check_index_type=True, check_column_type=True)
        with pytest.raises(ValueError):
            store.put('df2', df, format='table', data_columns=['A'])
        with pytest.raises(ValueError):
            store.put('df3', df, format='table', data_columns=True)
    with ensure_clean_store(setup_path) as store:
        store.append('df2', df)
        store.append('df2', df)
        tm.assert_frame_equal(store['df2'], concat((df, df)))
    df = DataFrame(np.arange(12).reshape(3, 4), columns=Index(list('ABCD'), name='foo'))
    expected = df.copy()
    if isinstance(expected.index, RangeIndex):
        expected.index = Int64Index(expected.index)
    with ensure_clean_store(setup_path) as store:
        store.put('df1', df, format='table')
        tm.assert_frame_equal(store['df1'], expected, check_index_type=True, check_column_type=True)