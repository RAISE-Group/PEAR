def test_multiple_open_close(self, setup_path):
    with ensure_clean_path(setup_path) as path:
        df = tm.makeDataFrame()
        df.to_hdf(path, 'df', mode='w', format='table')
        store = HDFStore(path)
        assert 'CLOSED' not in store.info()
        assert store.is_open
        store.close()
        assert 'CLOSED' in store.info()
        assert not store.is_open
    with ensure_clean_path(setup_path) as path:
        if pytables._table_file_open_policy_is_strict:
            store1 = HDFStore(path)
            with pytest.raises(ValueError):
                HDFStore(path)
            store1.close()
        else:
            store1 = HDFStore(path)
            store2 = HDFStore(path)
            assert 'CLOSED' not in store1.info()
            assert 'CLOSED' not in store2.info()
            assert store1.is_open
            assert store2.is_open
            store1.close()
            assert 'CLOSED' in store1.info()
            assert not store1.is_open
            assert 'CLOSED' not in store2.info()
            assert store2.is_open
            store2.close()
            assert 'CLOSED' in store1.info()
            assert 'CLOSED' in store2.info()
            assert not store1.is_open
            assert not store2.is_open
            store = HDFStore(path, mode='w')
            store.append('df', df)
            store2 = HDFStore(path)
            store2.append('df2', df)
            store2.close()
            assert 'CLOSED' in store2.info()
            assert not store2.is_open
            store.close()
            assert 'CLOSED' in store.info()
            assert not store.is_open
            store = HDFStore(path, mode='w')
            store.append('df', df)
            store2 = HDFStore(path)
            store.close()
            assert 'CLOSED' in store.info()
            assert not store.is_open
            store2.close()
            assert 'CLOSED' in store2.info()
            assert not store2.is_open
    with ensure_clean_path(setup_path) as path:
        df = tm.makeDataFrame()
        df.to_hdf(path, 'df', mode='w', format='table')
        store = HDFStore(path)
        store.close()
        with pytest.raises(ClosedFileError):
            store.keys()
        with pytest.raises(ClosedFileError):
            'df' in store
        with pytest.raises(ClosedFileError):
            len(store)
        with pytest.raises(ClosedFileError):
            store['df']
        with pytest.raises(AttributeError):
            store.df
        with pytest.raises(ClosedFileError):
            store.select('df')
        with pytest.raises(ClosedFileError):
            store.get('df')
        with pytest.raises(ClosedFileError):
            store.append('df2', df)
        with pytest.raises(ClosedFileError):
            store.put('df3', df)
        with pytest.raises(ClosedFileError):
            store.get_storer('df2')
        with pytest.raises(ClosedFileError):
            store.remove('df2')
        with pytest.raises(ClosedFileError, match='file is not open'):
            store.select('df')