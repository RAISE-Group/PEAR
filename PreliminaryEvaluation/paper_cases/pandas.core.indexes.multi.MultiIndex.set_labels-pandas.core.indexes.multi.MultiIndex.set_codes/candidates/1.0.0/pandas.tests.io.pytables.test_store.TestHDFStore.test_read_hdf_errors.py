def test_read_hdf_errors(self, setup_path):
    df = DataFrame(np.random.rand(4, 5), index=list('abcd'), columns=list('ABCDE'))
    with ensure_clean_path(setup_path) as path:
        with pytest.raises(IOError):
            read_hdf(path, 'key')
        df.to_hdf(path, 'df')
        store = HDFStore(path, mode='r')
        store.close()
        with pytest.raises(IOError):
            read_hdf(store, 'df')