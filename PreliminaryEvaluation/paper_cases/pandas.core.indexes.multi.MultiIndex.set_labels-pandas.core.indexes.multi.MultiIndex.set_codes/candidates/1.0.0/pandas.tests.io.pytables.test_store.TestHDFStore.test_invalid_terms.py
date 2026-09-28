def test_invalid_terms(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        with catch_warnings(record=True):
            df = tm.makeTimeDataFrame()
            df['string'] = 'foo'
            df.loc[0:4, 'string'] = 'bar'
            store.put('df', df, format='table')
            with pytest.raises(TypeError):
                Term()
            with pytest.raises(ValueError):
                store.select('df', 'df.index[3]')
            with pytest.raises(SyntaxError):
                store.select('df', 'index>')
    with ensure_clean_path(setup_path) as path:
        dfq = DataFrame(np.random.randn(10, 4), columns=list('ABCD'), index=date_range('20130101', periods=10))
        dfq.to_hdf(path, 'dfq', format='table', data_columns=True)
        read_hdf(path, 'dfq', where="index>Timestamp('20130104') & columns=['A', 'B']")
        read_hdf(path, 'dfq', where='A>0 or C>0')
    with ensure_clean_path(setup_path) as path:
        dfq = DataFrame(np.random.randn(10, 4), columns=list('ABCD'), index=date_range('20130101', periods=10))
        dfq.to_hdf(path, 'dfq', format='table')
        with pytest.raises(ValueError):
            read_hdf(path, 'dfq', where='A>0 or C>0')