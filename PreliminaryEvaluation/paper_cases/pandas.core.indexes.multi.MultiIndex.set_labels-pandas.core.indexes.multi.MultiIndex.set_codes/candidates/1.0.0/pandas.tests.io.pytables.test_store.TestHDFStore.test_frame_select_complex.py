def test_frame_select_complex(self, setup_path):
    df = tm.makeTimeDataFrame()
    df['string'] = 'foo'
    df.loc[df.index[0:4], 'string'] = 'bar'
    with ensure_clean_store(setup_path) as store:
        store.put('df', df, format='table', data_columns=['string'])
        result = store.select('df', 'index>df.index[3] & string="bar"')
        expected = df.loc[(df.index > df.index[3]) & (df.string == 'bar')]
        tm.assert_frame_equal(result, expected)
        result = store.select('df', 'index>df.index[3] & string="foo"')
        expected = df.loc[(df.index > df.index[3]) & (df.string == 'foo')]
        tm.assert_frame_equal(result, expected)
        result = store.select('df', 'index>df.index[3] | string="bar"')
        expected = df.loc[(df.index > df.index[3]) | (df.string == 'bar')]
        tm.assert_frame_equal(result, expected)
        result = store.select('df', '(index>df.index[3] & index<=df.index[6]) | string="bar"')
        expected = df.loc[(df.index > df.index[3]) & (df.index <= df.index[6]) | (df.string == 'bar')]
        tm.assert_frame_equal(result, expected)
        result = store.select('df', 'string!="bar"')
        expected = df.loc[df.string != 'bar']
        tm.assert_frame_equal(result, expected)
        with pytest.raises(NotImplementedError):
            store.select('df', '~(string="bar")')
        result = store.select('df', "~(columns=['A','B'])")
        expected = df.loc[:, df.columns.difference(['A', 'B'])]
        tm.assert_frame_equal(result, expected)
        result = store.select('df', "index>df.index[3] & columns in ['A','B']")
        expected = df.loc[df.index > df.index[3]].reindex(columns=['A', 'B'])
        tm.assert_frame_equal(result, expected)