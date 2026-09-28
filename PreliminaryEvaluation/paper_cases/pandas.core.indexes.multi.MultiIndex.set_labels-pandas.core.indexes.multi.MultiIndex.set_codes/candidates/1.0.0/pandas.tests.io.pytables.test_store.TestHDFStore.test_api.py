def test_api(self, setup_path):
    with ensure_clean_path(setup_path) as path:
        df = tm.makeDataFrame()
        df.iloc[:10].to_hdf(path, 'df', append=True, format='table')
        df.iloc[10:].to_hdf(path, 'df', append=True, format='table')
        tm.assert_frame_equal(read_hdf(path, 'df'), df)
        df.iloc[:10].to_hdf(path, 'df', append=False, format='table')
        df.iloc[10:].to_hdf(path, 'df', append=True, format='table')
        tm.assert_frame_equal(read_hdf(path, 'df'), df)
    with ensure_clean_path(setup_path) as path:
        df = tm.makeDataFrame()
        df.iloc[:10].to_hdf(path, 'df', append=True)
        df.iloc[10:].to_hdf(path, 'df', append=True, format='table')
        tm.assert_frame_equal(read_hdf(path, 'df'), df)
        df.iloc[:10].to_hdf(path, 'df', append=False, format='table')
        df.iloc[10:].to_hdf(path, 'df', append=True)
        tm.assert_frame_equal(read_hdf(path, 'df'), df)
    with ensure_clean_path(setup_path) as path:
        df = tm.makeDataFrame()
        df.to_hdf(path, 'df', append=False, format='fixed')
        tm.assert_frame_equal(read_hdf(path, 'df'), df)
        df.to_hdf(path, 'df', append=False, format='f')
        tm.assert_frame_equal(read_hdf(path, 'df'), df)
        df.to_hdf(path, 'df', append=False)
        tm.assert_frame_equal(read_hdf(path, 'df'), df)
        df.to_hdf(path, 'df')
        tm.assert_frame_equal(read_hdf(path, 'df'), df)
    with ensure_clean_store(setup_path) as store:
        path = store._path
        df = tm.makeDataFrame()
        _maybe_remove(store, 'df')
        store.append('df', df.iloc[:10], append=True, format='table')
        store.append('df', df.iloc[10:], append=True, format='table')
        tm.assert_frame_equal(store.select('df'), df)
        _maybe_remove(store, 'df')
        store.append('df', df.iloc[:10], append=False, format='table')
        store.append('df', df.iloc[10:], append=True, format='table')
        tm.assert_frame_equal(store.select('df'), df)
        _maybe_remove(store, 'df')
        store.append('df', df.iloc[:10], append=False, format='table')
        store.append('df', df.iloc[10:], append=True, format='table')
        tm.assert_frame_equal(store.select('df'), df)
        _maybe_remove(store, 'df')
        store.append('df', df.iloc[:10], append=False, format='table')
        store.append('df', df.iloc[10:], append=True, format=None)
        tm.assert_frame_equal(store.select('df'), df)
    with ensure_clean_path(setup_path) as path:
        df = tm.makeDataFrame()
        msg = 'Can only append to Tables'
        with pytest.raises(ValueError, match=msg):
            df.to_hdf(path, 'df', append=True, format='f')
        with pytest.raises(ValueError, match=msg):
            df.to_hdf(path, 'df', append=True, format='fixed')
        msg = 'invalid HDFStore format specified \\[foo\\]'
        with pytest.raises(TypeError, match=msg):
            df.to_hdf(path, 'df', append=True, format='foo')
        with pytest.raises(TypeError, match=msg):
            df.to_hdf(path, 'df', append=False, format='foo')
    path = ''
    msg = f'File {path} does not exist'
    with pytest.raises(FileNotFoundError, match=msg):
        read_hdf(path, 'df')