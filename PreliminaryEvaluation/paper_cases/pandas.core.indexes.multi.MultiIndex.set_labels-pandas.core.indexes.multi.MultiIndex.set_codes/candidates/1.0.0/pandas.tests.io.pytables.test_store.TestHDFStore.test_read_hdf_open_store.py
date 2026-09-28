def test_read_hdf_open_store(self, setup_path):
    df = DataFrame(np.random.rand(4, 5), index=list('abcd'), columns=list('ABCDE'))
    df.index.name = 'letters'
    df = df.set_index(keys='E', append=True)
    with ensure_clean_path(setup_path) as path:
        df.to_hdf(path, 'df', mode='w')
        direct = read_hdf(path, 'df')
        store = HDFStore(path, mode='r')
        indirect = read_hdf(store, 'df')
        tm.assert_frame_equal(direct, indirect)
        assert store.is_open
        store.close()