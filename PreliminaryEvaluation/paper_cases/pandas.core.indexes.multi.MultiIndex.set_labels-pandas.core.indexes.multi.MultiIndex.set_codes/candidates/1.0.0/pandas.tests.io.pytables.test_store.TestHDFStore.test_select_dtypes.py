def test_select_dtypes(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        df = DataFrame(dict(ts=bdate_range('2012-01-01', periods=300), A=np.random.randn(300)))
        _maybe_remove(store, 'df')
        store.append('df', df, data_columns=['ts', 'A'])
        result = store.select('df', "ts>=Timestamp('2012-02-01')")
        expected = df[df.ts >= Timestamp('2012-02-01')]
        tm.assert_frame_equal(expected, result)
        df = DataFrame(np.random.randn(5, 2), columns=['A', 'B'])
        df['object'] = 'foo'
        df.loc[4:5, 'object'] = 'bar'
        df['boolv'] = df['A'] > 0
        _maybe_remove(store, 'df')
        store.append('df', df, data_columns=True)
        expected = df[df.boolv == True].reindex(columns=['A', 'boolv'])
        for v in [True, 'true', 1]:
            result = store.select('df', 'boolv == {v!s}'.format(v=v), columns=['A', 'boolv'])
            tm.assert_frame_equal(expected, result)
        expected = df[df.boolv == False].reindex(columns=['A', 'boolv'])
        for v in [False, 'false', 0]:
            result = store.select('df', 'boolv == {v!s}'.format(v=v), columns=['A', 'boolv'])
            tm.assert_frame_equal(expected, result)
        df = DataFrame(dict(A=np.random.rand(20), B=np.random.rand(20)))
        _maybe_remove(store, 'df_int')
        store.append('df_int', df)
        result = store.select('df_int', "index<10 and columns=['A']")
        expected = df.reindex(index=list(df.index)[0:10], columns=['A'])
        tm.assert_frame_equal(expected, result)
        df = DataFrame(dict(A=np.random.rand(20), B=np.random.rand(20), index=np.arange(20, dtype='f8')))
        _maybe_remove(store, 'df_float')
        store.append('df_float', df)
        result = store.select('df_float', "index<10.0 and columns=['A']")
        expected = df.reindex(index=list(df.index)[0:10], columns=['A'])
        tm.assert_frame_equal(expected, result)
    with ensure_clean_store(setup_path) as store:
        df = DataFrame(dict(cols=range(11), values=range(11)), dtype='float64')
        df['cols'] = (df['cols'] + 10).apply(str)
        store.append('df1', df, data_columns=True)
        result = store.select('df1', where='values>2.0')
        expected = df[df['values'] > 2.0]
        tm.assert_frame_equal(expected, result)
        df.iloc[0] = np.nan
        expected = df[df['values'] > 2.0]
        store.append('df2', df, data_columns=True, index=False)
        result = store.select('df2', where='values>2.0')
        tm.assert_frame_equal(expected, result)
        df = DataFrame(dict(cols=range(11), values=range(11)), dtype='float64')
        df['cols'] = (df['cols'] + 10).apply(str)
        df.iloc[1] = np.nan
        expected = df[df['values'] > 2.0]
        store.append('df4', df, data_columns=True)
        result = store.select('df4', where='values>2.0')
        tm.assert_frame_equal(expected, result)
    with ensure_clean_store(setup_path) as store:
        df = tm.makeDataFrame()
        expected = df[df['A'] > 0]
        store.append('df', df, data_columns=True)
        np_zero = np.float64(0)
        result = store.select('df', where=['A>np_zero'])
        tm.assert_frame_equal(expected, result)