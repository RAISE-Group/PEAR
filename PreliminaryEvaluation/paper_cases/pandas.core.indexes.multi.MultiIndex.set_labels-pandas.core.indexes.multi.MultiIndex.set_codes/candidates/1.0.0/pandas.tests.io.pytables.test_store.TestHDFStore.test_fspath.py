def test_fspath(self):
    with tm.ensure_clean('foo.h5') as path:
        with pd.HDFStore(path) as store:
            assert os.fspath(store) == str(path)