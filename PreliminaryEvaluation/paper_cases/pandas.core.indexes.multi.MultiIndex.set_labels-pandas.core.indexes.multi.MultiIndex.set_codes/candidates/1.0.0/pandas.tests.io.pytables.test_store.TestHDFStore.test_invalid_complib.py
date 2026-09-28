def test_invalid_complib(self, setup_path):
    df = DataFrame(np.random.rand(4, 5), index=list('abcd'), columns=list('ABCDE'))
    with ensure_clean_path(setup_path) as path:
        with pytest.raises(ValueError):
            df.to_hdf(path, 'df', complib='foolib')