def test_unimplemented_dtypes_table_columns(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        dtypes = [('date', datetime.date(2001, 1, 2))]
        for n, f in dtypes:
            df = tm.makeDataFrame()
            df[n] = f
            with pytest.raises(TypeError):
                store.append('df1_{n}'.format(n=n), df)
    df = tm.makeDataFrame()
    df['obj1'] = 'foo'
    df['obj2'] = 'bar'
    df['datetime1'] = datetime.date(2001, 1, 2)
    df = df._consolidate()._convert(datetime=True)
    with ensure_clean_store(setup_path) as store:
        with pytest.raises(TypeError):
            store.append('df_unimplemented', df)