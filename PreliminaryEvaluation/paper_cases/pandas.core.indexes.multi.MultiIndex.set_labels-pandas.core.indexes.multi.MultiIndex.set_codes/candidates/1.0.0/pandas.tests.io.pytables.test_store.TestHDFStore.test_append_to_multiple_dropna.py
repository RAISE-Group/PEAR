def test_append_to_multiple_dropna(self, setup_path):
    df1 = tm.makeTimeDataFrame()
    df2 = tm.makeTimeDataFrame().rename(columns='{}_2'.format)
    df1.iloc[1, df1.columns.get_indexer(['A', 'B'])] = np.nan
    df = concat([df1, df2], axis=1)
    with ensure_clean_store(setup_path) as store:
        store.append_to_multiple({'df1': ['A', 'B'], 'df2': None}, df, selector='df1', dropna=True)
        result = store.select_as_multiple(['df1', 'df2'])
        expected = df.dropna()
        tm.assert_frame_equal(result, expected)
        tm.assert_index_equal(store.select('df1').index, store.select('df2').index)