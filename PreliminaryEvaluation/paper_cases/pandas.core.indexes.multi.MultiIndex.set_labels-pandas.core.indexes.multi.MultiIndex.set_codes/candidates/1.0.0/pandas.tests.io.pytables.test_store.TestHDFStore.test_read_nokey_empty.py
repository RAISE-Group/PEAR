def test_read_nokey_empty(self, setup_path):
    with ensure_clean_path(setup_path) as path:
        store = HDFStore(path)
        store.close()
        with pytest.raises(ValueError):
            read_hdf(path)