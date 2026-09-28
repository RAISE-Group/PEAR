def test_select_with_many_inputs(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        df = DataFrame(dict(ts=bdate_range('2012-01-01', periods=300), A=np.random.randn(300), B=range(300), users=['a'] * 50 + ['b'] * 50 + ['c'] * 100 + ['a{i:03d}'.format(i=i) for i in range(100)]))
        _maybe_remove(store, 'df')
        store.append('df', df, data_columns=['ts', 'A', 'B', 'users'])
        result = store.select('df', "ts>=Timestamp('2012-02-01')")
        expected = df[df.ts >= Timestamp('2012-02-01')]
        tm.assert_frame_equal(expected, result)
        result = store.select('df', "ts>=Timestamp('2012-02-01') & users=['a','b','c']")
        expected = df[(df.ts >= Timestamp('2012-02-01')) & df.users.isin(['a', 'b', 'c'])]
        tm.assert_frame_equal(expected, result)
        selector = ['a', 'b', 'c'] + ['a{i:03d}'.format(i=i) for i in range(60)]
        result = store.select('df', "ts>=Timestamp('2012-02-01') and users=selector")
        expected = df[(df.ts >= Timestamp('2012-02-01')) & df.users.isin(selector)]
        tm.assert_frame_equal(expected, result)
        selector = range(100, 200)
        result = store.select('df', 'B=selector')
        expected = df[df.B.isin(selector)]
        tm.assert_frame_equal(expected, result)
        assert len(result) == 100
        selector = Index(df.ts[0:100].values)
        result = store.select('df', 'ts=selector')
        expected = df[df.ts.isin(selector.values)]
        tm.assert_frame_equal(expected, result)
        assert len(result) == 100