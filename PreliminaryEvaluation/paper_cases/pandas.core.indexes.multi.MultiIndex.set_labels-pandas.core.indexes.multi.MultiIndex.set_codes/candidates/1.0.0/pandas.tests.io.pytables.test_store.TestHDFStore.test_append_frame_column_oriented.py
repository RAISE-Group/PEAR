def test_append_frame_column_oriented(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        df = tm.makeTimeDataFrame()
        _maybe_remove(store, 'df1')
        store.append('df1', df.iloc[:, :2], axes=['columns'])
        store.append('df1', df.iloc[:, 2:])
        tm.assert_frame_equal(store['df1'], df)
        result = store.select('df1', 'columns=A')
        expected = df.reindex(columns=['A'])
        tm.assert_frame_equal(expected, result)
        result = store.select('df1', ('columns=A', 'index=df.index[0:4]'))
        expected = df.reindex(columns=['A'], index=df.index[0:4])
        tm.assert_frame_equal(expected, result)
        with pytest.raises(TypeError):
            store.select('df1', 'columns=A and index>df.index[4]')