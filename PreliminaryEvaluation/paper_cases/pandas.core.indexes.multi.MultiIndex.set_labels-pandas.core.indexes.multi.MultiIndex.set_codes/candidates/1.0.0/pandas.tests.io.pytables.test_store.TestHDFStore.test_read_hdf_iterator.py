def test_read_hdf_iterator(self, setup_path):
    df = DataFrame(np.random.rand(4, 5), index=list('abcd'), columns=list('ABCDE'))
    df.index.name = 'letters'
    df = df.set_index(keys='E', append=True)
    with ensure_clean_path(setup_path) as path:
        df.to_hdf(path, 'df', mode='w', format='t')
        direct = read_hdf(path, 'df')
        iterator = read_hdf(path, 'df', iterator=True)
        assert isinstance(iterator, TableIterator)
        indirect = next(iterator.__iter__())
        tm.assert_frame_equal(direct, indirect)
        iterator.store.close()