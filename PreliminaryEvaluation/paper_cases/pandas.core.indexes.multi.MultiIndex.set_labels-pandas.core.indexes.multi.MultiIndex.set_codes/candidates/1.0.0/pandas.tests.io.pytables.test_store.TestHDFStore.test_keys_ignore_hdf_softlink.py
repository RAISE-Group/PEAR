def test_keys_ignore_hdf_softlink(self, setup_path):
    with ensure_clean_store(setup_path) as store:
        df = DataFrame(dict(A=range(5), B=range(5)))
        store.put('df', df)
        assert store.keys() == ['/df']
        store._handle.create_soft_link(store._handle.root, 'symlink', 'df')
        assert store.keys() == ['/df']