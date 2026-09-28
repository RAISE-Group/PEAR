def test_append_raise(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        df = tm.makeDataFrame()
        df['invalid'] = [['a']] * len(df)
        assert df.dtypes['invalid'] == np.object_
        with pytest.raises(TypeError):
            store.append('df', df)
        df['invalid2'] = [['a']] * len(df)
        df['invalid3'] = [['a']] * len(df)
        with pytest.raises(TypeError):
            store.append('df', df)
        df = tm.makeDataFrame()
        s = Series(datetime.datetime(2001, 1, 2), index=df.index)
        s = s.astype(object)
        s[0:5] = np.nan
        df['invalid'] = s
        assert df.dtypes['invalid'] == np.object_
        with pytest.raises(TypeError):
            store.append('df', df)
        with pytest.raises(TypeError):
            store.append('df', np.arange(10))
        with pytest.raises(TypeError):
            store.append('df', Series(np.arange(10)))
        df = tm.makeDataFrame()
        store.append('df', df)
        df['foo'] = 'foo'
        with pytest.raises(ValueError):
            store.append('df', df)