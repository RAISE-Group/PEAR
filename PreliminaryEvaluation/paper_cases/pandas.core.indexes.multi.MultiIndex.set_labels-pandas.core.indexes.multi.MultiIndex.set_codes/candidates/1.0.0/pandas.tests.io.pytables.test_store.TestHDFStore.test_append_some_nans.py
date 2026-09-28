def test_append_some_nans(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        df = DataFrame({'A': Series(np.random.randn(20)).astype('int32'), 'A1': np.random.randn(20), 'A2': np.random.randn(20), 'B': 'foo', 'C': 'bar', 'D': Timestamp('20010101'), 'E': datetime.datetime(2001, 1, 2, 0, 0)}, index=np.arange(20))
        _maybe_remove(store, 'df1')
        df.loc[0:15, ['A1', 'B', 'D', 'E']] = np.nan
        store.append('df1', df[:10])
        store.append('df1', df[10:])
        tm.assert_frame_equal(store['df1'], df)
        df1 = df.copy()
        df1.loc[:, 'A1'] = np.nan
        _maybe_remove(store, 'df1')
        store.append('df1', df1[:10])
        store.append('df1', df1[10:])
        tm.assert_frame_equal(store['df1'], df1)
        df2 = df.copy()
        df2.loc[:, 'A2'] = np.nan
        _maybe_remove(store, 'df2')
        store.append('df2', df2[:10])
        store.append('df2', df2[10:])
        tm.assert_frame_equal(store['df2'], df2)
        df3 = df.copy()
        df3.loc[:, 'E'] = np.nan
        _maybe_remove(store, 'df3')
        store.append('df3', df3[:10])
        store.append('df3', df3[10:])
        tm.assert_frame_equal(store['df3'], df3)