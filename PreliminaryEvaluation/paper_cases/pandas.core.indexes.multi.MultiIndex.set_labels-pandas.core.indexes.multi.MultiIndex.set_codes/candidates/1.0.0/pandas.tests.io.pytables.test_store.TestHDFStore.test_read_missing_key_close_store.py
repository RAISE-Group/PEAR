def test_read_missing_key_close_store(self, setup_path):
    with ensure_clean_path(setup_path) as path:
        df = pd.DataFrame({'a': range(2), 'b': range(2)})
        df.to_hdf(path, 'k1')
        with pytest.raises(KeyError, match="'No object named k2 in the file'"):
            pd.read_hdf(path, 'k2')
        df.to_hdf(path, 'k2')