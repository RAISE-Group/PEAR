@td.xfail_non_writeable
def test_append_misc(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        df = tm.makeDataFrame()
        store.append('df', df, chunksize=1)
        result = store.select('df')
        tm.assert_frame_equal(result, df)
        store.append('df1', df, expectedrows=10)
        result = store.select('df1')
        tm.assert_frame_equal(result, df)

    def check(obj, comparator):
        for c in [10, 200, 1000]:
            with ensure_clean_store(setup_path, mode='w') as store:
                store.append('obj', obj, chunksize=c)
                result = store.select('obj')
                comparator(result, obj)
    df = tm.makeDataFrame()
    df['string'] = 'foo'
    df['float322'] = 1.0
    df['float322'] = df['float322'].astype('float32')
    df['bool'] = df['float322'] > 0
    df['time1'] = Timestamp('20130101')
    df['time2'] = Timestamp('20130102')
    check(df, tm.assert_frame_equal)
    with ensure_clean_store(setup_path) as store:
        df_empty = DataFrame(columns=list('ABC'))
        store.append('df', df_empty)
        with pytest.raises(KeyError, match="'No object named df in the file'"):
            store.select('df')
        df = DataFrame(np.random.rand(10, 3), columns=list('ABC'))
        store.append('df', df)
        tm.assert_frame_equal(store.select('df'), df)
        store.append('df', df_empty)
        tm.assert_frame_equal(store.select('df'), df)
        df = DataFrame(columns=list('ABC'))
        store.put('df2', df)
        tm.assert_frame_equal(store.select('df2'), df)